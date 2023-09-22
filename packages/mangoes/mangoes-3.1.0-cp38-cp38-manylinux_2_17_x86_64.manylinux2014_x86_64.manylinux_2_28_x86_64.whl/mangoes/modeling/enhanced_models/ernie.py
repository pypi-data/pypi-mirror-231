import os
import math
import copy
import tarfile
import tagme
from transformers import BertTokenizer, BertPreTrainedModel, BatchEncoding
from transformers.modeling_outputs import BaseModelOutputWithPoolingAndCrossAttentions, SequenceClassifierOutput, \
    TokenClassifierOutput, QuestionAnsweringModelOutput, MultipleChoiceModelOutput
from transformers.models.bert.modeling_bert import BertEmbeddings, BertSelfAttention, BertSelfOutput, \
    BertPredictionHeadTransform, BertLMPredictionHead, BertPooler
from transformers.utils import PaddingStrategy
import numpy as np
import torch
from torch import nn
from torch.nn import BCEWithLogitsLoss, CrossEntropyLoss, MSELoss

from mangoes.utils.file_utils import download_and_cache, MANGOES_CACHE_PATH

tagme.GCUBE_TOKEN = "622c9fa2-f822-4dea-ac89-08ff01cb8afc-843339462"

ERNIE_DIR = os.path.join(MANGOES_CACHE_PATH, "ernie/")
ERNIE_MODEL_ARCHIVE_PATH = os.path.join(MANGOES_CACHE_PATH, "ernie/ernie_base.tar.gz")
ERNIE_KGEMB_ARCHIVE_PATH = os.path.join(MANGOES_CACHE_PATH, "ernie/kg_embed.tar.gz")
ERNIE_PRETRAINED_MODEL_DIR = os.path.join(ERNIE_DIR, "ernie_base")
ERNIE_PRETRAINED_KGEMB_DIR = os.path.join(ERNIE_DIR, "kg_embed")
ERNIE_MODEL_URL = "http://chercheurs.lille.inria.fr/magnet/ernie_base.tar.gz"
ERNIE_KGEMB_URL = "http://chercheurs.lille.inria.fr/magnet/kg_embed.tar.gz"


def download_extract_pretrained_ernie():
    """
    Downloads the the ernie pretrained weights and tokenizer.
    """
    if not os.path.exists(ERNIE_MODEL_ARCHIVE_PATH):
        print("Downloading ernie pretrained model...")
        download_and_cache(ERNIE_MODEL_URL, "ernie_base.tar.gz", cache_dir=ERNIE_DIR)
    if not os.path.exists(ERNIE_KGEMB_ARCHIVE_PATH):
        print("Downloading ernie knowledge graph embeddings...")
        download_and_cache(ERNIE_KGEMB_URL, "kg_embed.tar.gz", cache_dir=ERNIE_DIR)
    if not os.path.exists(ERNIE_PRETRAINED_MODEL_DIR):
        with tarfile.open(ERNIE_MODEL_ARCHIVE_PATH) as f:
            f.extractall(ERNIE_DIR)
    if not os.path.exists(os.path.join(ERNIE_PRETRAINED_MODEL_DIR, "config.json")):
        # rename config file to work with transformers from pretrained
        os.rename(os.path.join(ERNIE_PRETRAINED_MODEL_DIR, "ernie_config.json"),
                  os.path.join(ERNIE_PRETRAINED_MODEL_DIR, "config.json"))
    if not os.path.exists(ERNIE_PRETRAINED_KGEMB_DIR):
        with tarfile.open(ERNIE_KGEMB_ARCHIVE_PATH) as f:
            f.extractall(ERNIE_DIR)


class ErnieTokenizer(BertTokenizer):
    model_input_names = ["input_ids", "token_type_ids", "attention_mask", "entities", "entity_mask"]

    def __init__(
            self,
            vocab_file,
            entity_map_filepath=None,
            entity2id_filepath=None,
            do_lower_case=True,
            do_basic_tokenize=True,
            never_split=None,
            unk_token="[UNK]",
            sep_token="[SEP]",
            pad_token="[PAD]",
            cls_token="[CLS]",
            mask_token="[MASK]",
            tokenize_chinese_chars=True,
            strip_accents=None,
            **kwargs
    ):
        super().__init__(
            vocab_file,
            do_lower_case=do_lower_case,
            do_basic_tokenize=do_basic_tokenize,
            never_split=never_split,
            unk_token=unk_token,
            sep_token=sep_token,
            pad_token=pad_token,
            cls_token=cls_token,
            mask_token=mask_token,
            tokenize_chinese_chars=tokenize_chinese_chars,
            strip_accents=strip_accents,
            **kwargs
        )
        self.model_max_length = 512
        self.entity_name_to_id = {}
        with open(f"{ERNIE_PRETRAINED_KGEMB_DIR}/entity_map.txt" if entity_map_filepath is None
                  else entity_map_filepath) as f:
            for line in f:
                name, qid = line.strip().split("\t")
                self.entity_name_to_id[name] = qid
        self.entity_id_to_index = {}
        with open(f"{ERNIE_PRETRAINED_KGEMB_DIR}/entity2id.txt" if entity2id_filepath is None
                  else entity2id_filepath) as f:
            f.readline()
            for line in f:
                qid, eid = line.strip().split('\t')
                self.entity_id_to_index[qid] = int(eid)

    def _pad(self,
             encoded_inputs,
             max_length=None,
             padding_strategy=PaddingStrategy.DO_NOT_PAD,
             pad_to_multiple_of=None,
             return_attention_mask=None, ):
        if return_attention_mask is None:
            return_attention_mask = "attention_mask" in self.model_input_names
        required_input = encoded_inputs[self.model_input_names[0]]
        if padding_strategy == PaddingStrategy.LONGEST:
            max_length = len(required_input)
        if max_length is not None and pad_to_multiple_of is not None and (max_length % pad_to_multiple_of != 0):
            max_length = ((max_length // pad_to_multiple_of) + 1) * pad_to_multiple_of
        needs_to_be_padded = padding_strategy != PaddingStrategy.DO_NOT_PAD and len(required_input) != max_length
        if return_attention_mask and "attention_mask" not in encoded_inputs:
            encoded_inputs["attention_mask"] = [1] * len(required_input)
        if needs_to_be_padded:
            difference = max_length - len(required_input)
            if self.padding_side == "right":
                if return_attention_mask:
                    encoded_inputs["attention_mask"] = encoded_inputs["attention_mask"] + [0] * difference
                if "token_type_ids" in encoded_inputs:
                    encoded_inputs["token_type_ids"] = (
                            encoded_inputs["token_type_ids"] + [self.pad_token_type_id] * difference
                    )
                if "special_tokens_mask" in encoded_inputs:
                    encoded_inputs["special_tokens_mask"] = encoded_inputs["special_tokens_mask"] + [1] * difference
                if "entities" in encoded_inputs:
                    encoded_inputs["entities"] = encoded_inputs["entities"] + [-1] * difference
                if "entity_mask" in encoded_inputs:
                    encoded_inputs["entity_mask"] = encoded_inputs["entity_mask"] + [0] * difference
                encoded_inputs[self.model_input_names[0]] = required_input + [self.pad_token_id] * difference
            elif self.padding_side == "left":
                if return_attention_mask:
                    encoded_inputs["attention_mask"] = [0] * difference + encoded_inputs["attention_mask"]
                if "token_type_ids" in encoded_inputs:
                    encoded_inputs["token_type_ids"] = [self.pad_token_type_id] * difference + encoded_inputs[
                        "token_type_ids"
                    ]
                if "special_tokens_mask" in encoded_inputs:
                    encoded_inputs["special_tokens_mask"] = [1] * difference + encoded_inputs["special_tokens_mask"]
                if "entities" in encoded_inputs:
                    encoded_inputs["entities"] = [-1] * difference + encoded_inputs["entities"]
                if "entity_mask" in encoded_inputs:
                    encoded_inputs["entity_mask"] = [0] * difference + encoded_inputs["entity_mask"]

                encoded_inputs[self.model_input_names[0]] = [self.pad_token_id] * difference + required_input
            else:
                raise ValueError("Invalid padding strategy:" + str(self.padding_side))

        return encoded_inputs

    def process_entity_annotations(self, annotations, input_string, threshold=0.0):
        # processes tagme annotations: removes annotations with score less than threshold, converts char to word index
        ents = []
        tokens = input_string.split()
        current_char_index = 0
        char_index_to_token_index = {}
        for i in range(0, len(tokens)):
            for _ in range(len(tokens[i]) + 1):
                char_index_to_token_index[current_char_index] = i
                current_char_index += 1
        for a in annotations.get_annotations(threshold):
            if a.entity_title not in self.entity_name_to_id:
                continue
            ents.append([self.entity_name_to_id[a.entity_title], char_index_to_token_index[a.begin]])
        return ents

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, entity_map_filepath=None, entity2id_filepath=None,
                        *init_inputs, **kwargs):
        if pretrained_model_name_or_path is None or entity2id_filepath is None or entity_map_filepath is None:
            download_extract_pretrained_ernie()
        if pretrained_model_name_or_path is None:
            return super().from_pretrained(ERNIE_PRETRAINED_MODEL_DIR, *init_inputs,
                                           entity_map_filepath=entity_map_filepath,
                                           entity2id_filepath=entity2id_filepath, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *init_inputs,
                                           entity_map_filepath=entity_map_filepath,
                                           entity2id_filepath=entity2id_filepath, **kwargs)

    def save_pretrained(self, save_directory, legacy_format=None, filename_prefix=None, push_to_hub=False, **kwargs):
        super().save_pretrained(save_directory, legacy_format, filename_prefix, push_to_hub, **kwargs)
        remove_chars = len(os.linesep)
        with open(f"{save_directory}/entity_map.txt", 'a+') as f:
            for key, value in self.entity_name_to_id.items():
                f.write(f"{key}\t{value}\n")
            f.truncate(f.tell() - remove_chars)
        with open(f"{save_directory}/entity2id.txt", 'a+') as f:
            f.write("\n")  # blank line to get same format as pretrained ernie mapping
            for key, value in self.entity_id_to_index.items():
                f.write(f"{key}\t{value}\n")
            f.truncate(f.tell() - remove_chars)

    def __call__(self, text=None, text_pair=None, add_special_tokens=True, padding=False, truncation=None,
                 max_length=None, stride=0, is_split_into_words=False, pad_to_multiple_of=None, return_tensors=None,
                 return_token_type_ids=None, return_attention_mask=None,
                 return_overflowing_tokens=False, return_special_tokens_mask=False, return_offsets_mapping=False,
                 return_length=False, verbose=True, text_annotations=None, text_pair_annotations=None, **kwargs):
        if is_split_into_words:
            is_batched = isinstance(text, (list, tuple)) and isinstance(text[0], (list, tuple))
        else:
            is_batched = isinstance(text, (list, tuple))
        if text_annotations is None or (text_pair is not None and text_pair_annotations is None):
            if not is_batched:
                text = [text]
                if text_pair is not None:
                    text_pair = [text_pair]
            text_annotations = []
            text_pair_annotations = []
            for sequence in text:
                input_string = ' '.join(sequence) if is_split_into_words else ' '.join(sequence.split())
                text_annotations.append(self.process_entity_annotations(tagme.annotate(input_string), input_string))
            if text_pair is not None:
                for sequence in text_pair:
                    input_string = ' '.join(sequence) if is_split_into_words else ' '.join(sequence.split())
                    text_pair_annotations.append(self.process_entity_annotations(tagme.annotate(input_string),
                                                                                 input_string))
        elif not is_batched:
            text_annotations = [text_annotations]
            text = [text]
            if text_pair:
                text_pair = [text_pair]
                text_pair_annotations = [text_pair_annotations]
        tokenizer_output = \
            super(ErnieTokenizer, self).__call__(text=text, text_pair=text_pair,
                                                 add_special_tokens=add_special_tokens,
                                                 padding=padding, truncation=truncation,
                                                 max_length=max_length, stride=stride,
                                                 is_split_into_words=is_split_into_words,
                                                 pad_to_multiple_of=pad_to_multiple_of,
                                                 return_tensors=return_tensors,
                                                 return_token_type_ids=return_token_type_ids,
                                                 return_attention_mask=return_attention_mask,
                                                 return_overflowing_tokens=return_overflowing_tokens,
                                                 return_special_tokens_mask=return_special_tokens_mask,
                                                 return_offsets_mapping=return_offsets_mapping,
                                                 return_length=return_length, verbose=verbose, **kwargs)
        ent_sequences = []
        ent_mask = []
        token_input_sequence = tokenizer_output["input_ids"]
        for i in range(len(token_input_sequence)):
            current_ent_sequence = [-1] * len(token_input_sequence[i])
            current_ent_mask = [0] * len(token_input_sequence[i])
            sequence_subtokens = super(ErnieTokenizer, self).convert_ids_to_tokens(token_input_sequence[i])
            token_index_to_subtoken_index = {}
            current_token_index = 0
            current_subtoken_index = 1 if add_special_tokens else 0
            while current_subtoken_index < len(sequence_subtokens) and \
                    not sequence_subtokens[current_subtoken_index] == '[SEP]' and \
                    not sequence_subtokens[current_subtoken_index] == '[PAD]':
                if not sequence_subtokens[current_subtoken_index].startswith("##"):
                    token_index_to_subtoken_index[current_token_index] = current_subtoken_index
                    current_token_index += 1
                current_subtoken_index += 1
            for annotation in text_annotations[i]:
                if annotation[0] in self.entity_id_to_index:
                    current_ent_sequence[token_index_to_subtoken_index[annotation[1]]] = \
                        self.entity_id_to_index[annotation[0]]
                    current_ent_mask[token_index_to_subtoken_index[annotation[1]]] = 1
            if text_pair is not None:
                token_index_to_subtoken_index = {}
                current_subtoken_index += 1
                current_token_index = 0
                while current_subtoken_index < len(sequence_subtokens) and \
                        not sequence_subtokens[current_subtoken_index] == '[SEP]' and \
                        not sequence_subtokens[current_subtoken_index] == '[PAD]':
                    if not sequence_subtokens[current_subtoken_index].startswith("##"):
                        token_index_to_subtoken_index[current_token_index] = current_subtoken_index
                        current_token_index += 1
                    current_subtoken_index += 1
                for annotation in text_pair_annotations[i]:
                    if annotation[0] in self.entity_id_to_index:
                        current_ent_sequence[token_index_to_subtoken_index[annotation[1]]] = \
                            self.entity_id_to_index[annotation[0]]
                        current_ent_mask[token_index_to_subtoken_index[annotation[1]]] = 1
            ent_sequences.append(current_ent_sequence)
            ent_mask.append(current_ent_mask)
        tokenizer_output_dict = {k: v[0] if not is_batched and return_tensors is None else v for k, v in
                                 tokenizer_output.items()}
        tokenizer_output_dict.update(
            {"entities": ent_sequences[0] if not is_batched and return_tensors is None else ent_sequences,
             "entity_mask": ent_mask[0] if not is_batched and return_tensors is None else ent_mask})
        return BatchEncoding(tokenizer_output_dict, tensor_type=return_tensors)


def gelu(x):
    """Implementation of the gelu activation function.
        For information: OpenAI GPT's gelu is slightly different (and gives slightly different results):
        0.5 * x * (1 + torch.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * torch.pow(x, 3))))
    """
    return x * 0.5 * (1.0 + torch.erf(x / math.sqrt(2.0)))


def swish(x):
    return x * torch.sigmoid(x)


ACT2FN = {"gelu": gelu, "relu": torch.nn.functional.relu, "swish": swish}


class ErnieLayerNorm(nn.Module):
    def __init__(self, hidden_size, eps=1e-12):
        """Construct a layernorm module in the TF style (epsilon inside the square root).
        """
        super(ErnieLayerNorm, self).__init__()
        self.weight = nn.Parameter(torch.ones(hidden_size))
        self.bias = nn.Parameter(torch.zeros(hidden_size))
        self.variance_epsilon = eps

    def forward(self, x):
        u = x.mean(-1, keepdim=True)
        s = (x - u).pow(2).mean(-1, keepdim=True)
        x = (x - u) / torch.sqrt(s + self.variance_epsilon)
        return self.weight * x + self.bias


class ErnieAttention(nn.Module):
    def __init__(self, config):
        super(ErnieAttention, self).__init__()
        self.self = BertSelfAttention(config)
        self.output = BertSelfOutput(config)

        config_ent = copy.deepcopy(config)
        config_ent.hidden_size = 100
        config_ent.num_attention_heads = 4

        self.self_ent = BertSelfAttention(config_ent)
        self.output_ent = BertSelfOutput(config_ent)

    def forward(self, input_tensor, attention_mask, input_tensor_ent, attention_mask_ent):
        self_output = self.self(input_tensor, attention_mask)
        self_output_ent = self.self_ent(input_tensor_ent, attention_mask_ent)
        attention_output = self.output(self_output[0], input_tensor)
        attention_output_ent = self.output_ent(self_output_ent[0], input_tensor_ent)
        return attention_output, attention_output_ent


class ErnieAttention_simple(nn.Module):
    def __init__(self, config):
        super(ErnieAttention_simple, self).__init__()
        self.self = BertSelfAttention(config)
        self.output = BertSelfOutput(config)

    def forward(self, input_tensor, attention_mask):
        self_output = self.self(input_tensor, attention_mask)
        attention_output = self.output(self_output[0], input_tensor)
        return attention_output


class ErnieIntermediate(nn.Module):
    def __init__(self, config):
        super(ErnieIntermediate, self).__init__()
        self.dense = nn.Linear(config.hidden_size, config.intermediate_size)
        self.dense_ent = nn.Linear(100, config.intermediate_size)
        self.intermediate_act_fn = ACT2FN[config.hidden_act] \
            if isinstance(config.hidden_act, str) else config.hidden_act

    def forward(self, hidden_states, hidden_states_ent):
        hidden_states_ = self.dense(hidden_states)
        hidden_states_ent_ = self.dense_ent(hidden_states_ent)
        hidden_states = self.intermediate_act_fn(hidden_states_ + hidden_states_ent_)
        return hidden_states


class ErnieIntermediate_simple(nn.Module):
    def __init__(self, config):
        super(ErnieIntermediate_simple, self).__init__()
        self.dense = nn.Linear(config.hidden_size, config.intermediate_size)
        self.intermediate_act_fn = ACT2FN[config.hidden_act] \
            if isinstance(config.hidden_act, str) else config.hidden_act

    def forward(self, hidden_states):
        hidden_states = self.dense(hidden_states)
        hidden_states = self.intermediate_act_fn(hidden_states)
        return hidden_states


class ErnieOutput(nn.Module):
    def __init__(self, config):
        super(ErnieOutput, self).__init__()
        self.dense = nn.Linear(config.intermediate_size, config.hidden_size)
        self.dense_ent = nn.Linear(config.intermediate_size, 100)
        self.LayerNorm = ErnieLayerNorm(config.hidden_size, eps=1e-12)
        self.LayerNorm_ent = ErnieLayerNorm(100, eps=1e-12)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

    def forward(self, hidden_states_, input_tensor, input_tensor_ent):
        hidden_states = self.dense(hidden_states_)
        hidden_states = self.dropout(hidden_states)
        hidden_states = self.LayerNorm(hidden_states + input_tensor)

        hidden_states_ent = self.dense_ent(hidden_states_)
        hidden_states_ent = self.dropout(hidden_states_ent)
        hidden_states_ent = self.LayerNorm_ent(hidden_states_ent + input_tensor_ent)

        return hidden_states, hidden_states_ent


class ErnieOutput_simple(nn.Module):
    def __init__(self, config):
        super(ErnieOutput_simple, self).__init__()
        self.dense = nn.Linear(config.intermediate_size, config.hidden_size)
        self.LayerNorm = ErnieLayerNorm(config.hidden_size, eps=1e-12)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

    def forward(self, hidden_states, input_tensor):
        hidden_states = self.dense(hidden_states)
        hidden_states = self.dropout(hidden_states)
        hidden_states = self.LayerNorm(hidden_states + input_tensor)

        return hidden_states


class ErnieLayerMix(nn.Module):
    def __init__(self, config):
        super(ErnieLayerMix, self).__init__()
        self.attention = ErnieAttention_simple(config)
        self.intermediate = ErnieIntermediate(config)
        self.output = ErnieOutput(config)

    def forward(self, hidden_states, attention_mask, hidden_states_ent, attention_mask_ent, ent_mask):
        attention_output = self.attention(hidden_states, attention_mask)
        attention_output_ent = hidden_states_ent * ent_mask
        intermediate_output = self.intermediate(attention_output, attention_output_ent)
        layer_output, layer_output_ent = self.output(intermediate_output, attention_output, attention_output_ent)
        # layer_output_ent = layer_output_ent * ent_mask
        return layer_output, layer_output_ent


class ErnieLayer(nn.Module):
    def __init__(self, config):
        super(ErnieLayer, self).__init__()
        self.attention = ErnieAttention(config)
        self.intermediate = ErnieIntermediate(config)
        self.output = ErnieOutput(config)

    def forward(self, hidden_states, attention_mask, hidden_states_ent, attention_mask_ent, ent_mask):
        attention_output, attention_output_ent = self.attention(hidden_states, attention_mask, hidden_states_ent,
                                                                attention_mask_ent)
        attention_output_ent = attention_output_ent * ent_mask
        intermediate_output = self.intermediate(attention_output, attention_output_ent)
        layer_output, layer_output_ent = self.output(intermediate_output, attention_output, attention_output_ent)
        # layer_output_ent = layer_output_ent * ent_mask
        return layer_output, layer_output_ent


class ErnieLayer_simple(nn.Module):
    def __init__(self, config):
        super(ErnieLayer_simple, self).__init__()
        self.attention = ErnieAttention_simple(config)
        self.intermediate = ErnieIntermediate_simple(config)
        self.output = ErnieOutput_simple(config)

    def forward(self, hidden_states, attention_mask, hidden_states_ent, attention_mask_ent, ent_mask):
        attention_output = self.attention(hidden_states, attention_mask)
        intermediate_output = self.intermediate(attention_output)
        layer_output = self.output(intermediate_output, attention_output)
        return layer_output, hidden_states_ent


class ErnieEncoder(nn.Module):
    def __init__(self, config):
        super(ErnieEncoder, self).__init__()
        layer = ErnieLayer(config)
        layer_simple = ErnieLayer_simple(config)
        layer_mix = ErnieLayerMix(config)
        layers = []
        for t in config.layer_types:
            if t == "sim":
                layers.append(copy.deepcopy(layer_simple))
            if t == "norm":
                layers.append(copy.deepcopy(layer))
            if t == "mix":
                layers.append(copy.deepcopy(layer_mix))
        for _ in range(config.num_hidden_layers - len(layers)):
            layers.append(copy.deepcopy(layer_simple))
        self.layer = nn.ModuleList(layers)

    def forward(self, hidden_states, attention_mask, hidden_states_ent, attention_mask_ent, ent_mask,
                output_all_encoded_layers=True):
        all_encoder_layers = [hidden_states]
        ent_mask = ent_mask.to(dtype=next(self.parameters()).dtype).unsqueeze(-1)
        for layer_module in self.layer:
            hidden_states, hidden_states_ent = layer_module(hidden_states, attention_mask, hidden_states_ent,
                                                            attention_mask_ent, ent_mask)
            if output_all_encoded_layers:
                all_encoder_layers.append(hidden_states)
        if not output_all_encoded_layers:
            all_encoder_layers.append(hidden_states)
        return all_encoder_layers


class ErnieEntPredictionHead(nn.Module):
    def __init__(self, config):
        super(ErnieEntPredictionHead, self).__init__()
        config_ent = copy.deepcopy(config)
        config_ent.hidden_size = 100
        self.transform = BertPredictionHeadTransform(config_ent)

    def forward(self, hidden_states, candidate):
        hidden_states = self.transform(hidden_states)
        candidate = torch.squeeze(candidate, 0)
        # hidden_states [batch_size, max_seq, dim]
        # candidate [entity_num_in_the_batch, dim]
        # return [batch_size, max_seq, entity_num_in_the_batch]
        return torch.matmul(hidden_states, candidate.t())


class ErniePreTrainingHeads(nn.Module):
    def __init__(self, config, bert_model_embedding_weights):
        super(ErniePreTrainingHeads, self).__init__()
        self.predictions = BertLMPredictionHead(config)
        self.predictions_ent = ErnieEntPredictionHead(config)
        self.seq_relationship = nn.Linear(config.hidden_size, 2)

    def forward(self, sequence_output, pooled_output, candidate):
        prediction_scores = self.predictions(sequence_output)
        seq_relationship_score = self.seq_relationship(pooled_output)
        prediction_scores_ent = self.predictions_ent(sequence_output, candidate)
        return prediction_scores, seq_relationship_score, prediction_scores_ent


class ErniePreTrainedModel(BertPreTrainedModel):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_pretrained_ernie()
            return super().from_pretrained(ERNIE_PRETRAINED_MODEL_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class ErnieModel(ErniePreTrainedModel):
    def __init__(self, config, kg_embeddings=None):
        super(ErnieModel, self).__init__(config)
        self.embeddings = BertEmbeddings(config)
        self.encoder = ErnieEncoder(config)
        self.pooler = BertPooler(config)
        self.init_weights()
        if kg_embeddings is not None:
            embed = torch.FloatTensor(kg_embeddings)
            embed = torch.nn.Embedding.from_pretrained(embed)
            self.kg_embeddings = embed
        else:
            self.kg_embeddings = None

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, kg_embeddings=None, **kwargs):
        model = super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)
        if kg_embeddings is None:
            kg_embeddings = np.load(f"{ERNIE_PRETRAINED_KGEMB_DIR}/ernie_kg_embeddings.npy")
        embed = torch.FloatTensor(kg_embeddings)
        embed = torch.nn.Embedding.from_pretrained(embed)
        model.kg_embeddings = embed
        return model

    def forward(self, input_ids, attention_mask=None, token_type_ids=None, entities=None, entity_mask=None,
                output_attentions=None, output_hidden_states=None, return_dict=None):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict
        input_ent = self.kg_embeddings(entities + 1)
        if attention_mask is None:
            attention_mask = torch.ones_like(input_ids)
        if token_type_ids is None:
            token_type_ids = torch.zeros_like(input_ids)

        # We create a 3D attention mask from a 2D tensor mask.
        # Sizes are [batch_size, 1, 1, to_seq_length]
        # So we can broadcast to [batch_size, num_heads, from_seq_length, to_seq_length]
        # this attention mask is more simple than the triangular masking of causal attention
        # used in OpenAI GPT, we just need to prepare the broadcast dimension here.
        extended_attention_mask = attention_mask.unsqueeze(1).unsqueeze(2)
        extended_ent_mask = entity_mask.unsqueeze(1).unsqueeze(2)

        # Since attention_mask is 1.0 for positions we want to attend and 0.0 for
        # masked positions, this operation will create a tensor which is 0.0 for
        # positions we want to attend and -10000.0 for masked positions.
        # Since we are adding it to the raw scores before the softmax, this is
        # effectively the same as removing these entirely.
        extended_attention_mask = extended_attention_mask.to(dtype=next(self.parameters()).dtype)  # fp16 compatibility
        extended_attention_mask = (1.0 - extended_attention_mask) * -10000.0
        extended_ent_mask = extended_ent_mask.to(dtype=next(self.parameters()).dtype)  # fp16 compatibility
        extended_ent_mask = (1.0 - extended_ent_mask) * -10000.0

        embedding_output = self.embeddings(input_ids, token_type_ids)
        encoded_layers = self.encoder(embedding_output,
                                      extended_attention_mask,
                                      input_ent,
                                      extended_ent_mask,
                                      entity_mask,
                                      output_all_encoded_layers=output_hidden_states)
        sequence_output = encoded_layers[-1]
        pooled_output = self.pooler(sequence_output)
        if not return_dict:
            return (sequence_output, pooled_output) + (encoded_layers[1:],)

        return BaseModelOutputWithPoolingAndCrossAttentions(
            last_hidden_state=sequence_output,
            pooler_output=pooled_output,
            past_key_values=None,
            hidden_states=encoded_layers,
            attentions=None,
            cross_attentions=None,
        )


class ErnieForSequenceClassification(ErniePreTrainedModel):
    def __init__(self, config, kg_embeddings=None):
        super(ErnieForSequenceClassification, self).__init__(config)
        self.num_labels = config.num_labels
        self.bert = ErnieModel(config, kg_embeddings)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)
        self.init_weights()

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, kg_embeddings=None, labels=None, label2id=None,
                        **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        model = super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)
        if kg_embeddings is None:
            kg_embeddings = np.load(f"{ERNIE_PRETRAINED_KGEMB_DIR}/ernie_kg_embeddings.npy")
        embed = torch.FloatTensor(kg_embeddings)
        embed = torch.nn.Embedding.from_pretrained(embed)
        model.bert.kg_embeddings = embed
        return model

    def forward(self, input_ids, attention_mask=None, token_type_ids=None, entities=None, entity_mask=None,
                labels=None, output_attentions=None, output_hidden_states=None, return_dict=None):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            entities=entities,
            entity_mask=entity_mask,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        pooled_output = outputs[1]
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)

        loss = None
        if labels is not None:
            if self.config.problem_type is None:
                if self.num_labels == 1:
                    self.config.problem_type = "regression"
                elif self.num_labels > 1 and (labels.dtype == torch.long or labels.dtype == torch.int):
                    self.config.problem_type = "single_label_classification"
                else:
                    self.config.problem_type = "multi_label_classification"

            if self.config.problem_type == "regression":
                loss_fct = MSELoss()
                if self.num_labels == 1:
                    loss = loss_fct(logits.squeeze(), labels.squeeze())
                else:
                    loss = loss_fct(logits, labels)
            elif self.config.problem_type == "single_label_classification":
                loss_fct = CrossEntropyLoss()
                loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
            elif self.config.problem_type == "multi_label_classification":
                loss_fct = BCEWithLogitsLoss()
                loss = loss_fct(logits, labels)
        if not return_dict:
            output = (logits,) + outputs[2:]
            return ((loss,) + output) if loss is not None else output

        return SequenceClassifierOutput(
            loss=loss,
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )


class ErnieForTokenClassification(ErniePreTrainedModel):
    def __init__(self, config, kg_embeddings=None):
        super(ErnieForTokenClassification, self).__init__(config)
        self.num_labels = config.num_labels
        self.bert = ErnieModel(config, kg_embeddings)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)
        self.init_weights()

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, kg_embeddings=None, labels=None, label2id=None,
                        **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        model = super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)
        if kg_embeddings is None:
            kg_embeddings = np.load(f"{ERNIE_PRETRAINED_KGEMB_DIR}/ernie_kg_embeddings.npy")
        embed = torch.FloatTensor(kg_embeddings)
        embed = torch.nn.Embedding.from_pretrained(embed)
        model.bert.kg_embeddings = embed
        return model

    def forward(self, input_ids, attention_mask=None, token_type_ids=None, entities=None, entity_mask=None,
                labels=None, output_attentions=None, output_hidden_states=None, return_dict=None):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            entities=entities,
            entity_mask=entity_mask,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        sequence_output = self.dropout(outputs[0])
        logits = self.classifier(sequence_output)
        loss = None
        if labels is not None:
            loss_fct = CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
        if not return_dict:
            output = (logits,) + outputs[2:]
            return ((loss,) + output) if loss is not None else output
        return TokenClassifierOutput(
            loss=loss,
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )


class ErnieForQuestionAnswering(ErniePreTrainedModel):
    def __init__(self, config, kg_embeddings=None):
        super(ErnieForQuestionAnswering, self).__init__(config)
        self.bert = ErnieModel(config, kg_embeddings)
        self.qa_outputs = nn.Linear(config.hidden_size, 2)
        self.init_weights()

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, kg_embeddings=None, **kwargs):
        model = super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)
        if kg_embeddings is None:
            kg_embeddings = np.load(f"{ERNIE_PRETRAINED_KGEMB_DIR}/ernie_kg_embeddings.npy")
        embed = torch.FloatTensor(kg_embeddings)
        embed = torch.nn.Embedding.from_pretrained(embed)
        model.bert.kg_embeddings = embed
        return model

    def forward(self, input_ids, attention_mask=None, token_type_ids=None, entities=None, entity_mask=None,
                start_positions=None, end_positions=None, output_attentions=None, output_hidden_states=None,
                return_dict=None):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            entities=entities,
            entity_mask=entity_mask,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        logits = self.qa_outputs(outputs[0])
        start_logits, end_logits = logits.split(1, dim=-1)
        start_logits = start_logits.squeeze(-1)
        end_logits = end_logits.squeeze(-1)
        total_loss = None
        if start_positions is not None and end_positions is not None:
            if len(start_positions.size()) > 1:
                start_positions = start_positions.squeeze(-1)
            if len(end_positions.size()) > 1:
                end_positions = end_positions.squeeze(-1)
            # sometimes the start/end positions are outside our model inputs, we ignore these terms
            ignored_index = start_logits.size(1)
            start_positions.clamp_(0, ignored_index)
            end_positions.clamp_(0, ignored_index)
            loss_fct = CrossEntropyLoss(ignore_index=ignored_index)
            start_loss = loss_fct(start_logits, start_positions)
            end_loss = loss_fct(end_logits, end_positions)
            total_loss = (start_loss + end_loss) / 2
        if not return_dict:
            output = (start_logits, end_logits) + outputs[2:]
            return ((total_loss,) + output) if total_loss is not None else output
        return QuestionAnsweringModelOutput(
            loss=total_loss,
            start_logits=start_logits,
            end_logits=end_logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )


class ErnieForMultipleChoice(ErniePreTrainedModel):
    def __init__(self, config, num_choices=2, kg_embeddings=None):
        super(ErnieForMultipleChoice, self).__init__(config, kg_embeddings)
        self.num_choices = num_choices
        self.bert = ErnieModel(config, kg_embeddings)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, 1)
        self.init_weights()

    def forward(self, input_ids, attention_mask=None, token_type_ids=None, entities=None, entity_mask=None,
                labels=None, output_attentions=None, output_hidden_states=None,
                return_dict=None):
        flat_input_ids = input_ids.view(-1, input_ids.size(-1))
        flat_token_type_ids = token_type_ids.view(-1, token_type_ids.size(-1))
        flat_attention_mask = attention_mask.view(-1, attention_mask.size(-1))
        flat_entity_ids = entities.view(-1, entities.size(-1))
        flat_entity_mask = entity_mask.view(-1, entity_mask.size(-1))
        outputs = self.bert(flat_input_ids, flat_token_type_ids, flat_attention_mask, entities=flat_entity_ids,
                            entity_mask=flat_entity_mask,
                            output_attentions=output_attentions,
                            output_hidden_states=output_hidden_states,
                            return_dict=return_dict, )
        pooled_output = self.dropout(outputs[1])
        logits = self.classifier(pooled_output)
        reshaped_logits = logits.view(-1, self.num_choices)
        loss = None
        if labels is not None:
            loss_fct = CrossEntropyLoss()
            loss = loss_fct(reshaped_logits, labels)
        if not return_dict:
            output = (reshaped_logits,) + outputs[2:]
            return ((loss,) + output) if loss is not None else output
        else:
            return MultipleChoiceModelOutput(
                loss=loss,
                logits=reshaped_logits,
                hidden_states=outputs.hidden_states,
                attentions=outputs.attentions,
            )

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, kg_embeddings=None, **kwargs):
        model = super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)
        if kg_embeddings is None:
            kg_embeddings = np.load(f"{ERNIE_PRETRAINED_KGEMB_DIR}/ernie_kg_embeddings.npy")
        embed = torch.FloatTensor(kg_embeddings)
        embed = torch.nn.Embedding.from_pretrained(embed)
        model.bert.kg_embeddings = embed
        return model
