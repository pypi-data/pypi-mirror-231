import os
import tarfile
from ...utils.file_utils import download_and_cache, MANGOES_CACHE_PATH
import torch
import torch.nn as nn
from transformers.models.bert.modeling_bert import BertEncoder
from transformers.models.roberta.modeling_roberta import RobertaClassificationHead
from transformers.modeling_outputs import BaseModelOutputWithPoolingAndCrossAttentions
from transformers import RobertaModel, RobertaForSequenceClassification, \
    RobertaForTokenClassification, RobertaForQuestionAnswering, RobertaForMultipleChoice

KADAPTER_DIR = os.path.join(MANGOES_CACHE_PATH, "kadapter/")
KADAPTER_ARCHIVE_PATH = os.path.join(MANGOES_CACHE_PATH, "kadapter/pretrained_kadapter.tar.xz")
KADAPTER_PRETRAINED_DIR = os.path.join(KADAPTER_DIR, "pretrained_kadapter")
KADAPTER_URL = "http://chercheurs.lille.inria.fr/magnet/pretrained_kadapter.tar.xz"
KADAPTER_PRETRAINED_TOKENIZER_NAME = "roberta-large"


def download_extract_kadapter_weights():
    """
    Downloads the pretrained weights.
    """
    if not os.path.exists(KADAPTER_ARCHIVE_PATH):
        print("Downloading k-adapter pretrained model...")
        download_and_cache(KADAPTER_URL, "pretrained_kadapter.tar.xz", cache_dir=KADAPTER_DIR)
    if not os.path.exists(KADAPTER_PRETRAINED_DIR):
        with tarfile.open(KADAPTER_ARCHIVE_PATH) as f:
            f.extractall(KADAPTER_DIR)


class Adapter(nn.Module):
    def __init__(self, adapter_config):
        super(Adapter, self).__init__()
        self.adapter_config = adapter_config
        self.down_project = nn.Linear(
            self.adapter_config.project_hidden_size,
            self.adapter_config.adapter_size,
        )
        self.encoder = BertEncoder(self.adapter_config)
        self.up_project = nn.Linear(self.adapter_config.adapter_size, adapter_config.project_hidden_size)

    def forward(self, hidden_states):
        down_projected = self.down_project(hidden_states)

        input_shape = down_projected.size()[:-1]
        attention_mask = torch.ones(input_shape, device=next(self.parameters()).device)
        encoder_attention_mask = torch.ones(input_shape, device=next(self.parameters()).device)
        if attention_mask.dim() == 3:
            extended_attention_mask = attention_mask[:, None, :, :]
        if attention_mask.dim() == 2:
            extended_attention_mask = attention_mask[:, None, None, :]
        extended_attention_mask = extended_attention_mask.to(dtype=next(self.parameters()).dtype)  # fp16 compatibility
        extended_attention_mask = (1.0 - extended_attention_mask) * -10000.0

        if encoder_attention_mask.dim() == 3:
            encoder_extended_attention_mask = encoder_attention_mask[:, None, :, :]
        if encoder_attention_mask.dim() == 2:
            encoder_extended_attention_mask = encoder_attention_mask[:, None, None, :]
        head_mask = [None] * self.adapter_config.num_hidden_layers
        encoder_outputs = self.encoder(down_projected,
                                       attention_mask=extended_attention_mask,
                                       head_mask=head_mask)
        up_projected = self.up_project(encoder_outputs[0])
        return hidden_states + up_projected


class AdapterModel(nn.Module):
    def __init__(self, pretrained_model_config):
        super(AdapterModel, self).__init__()
        self.config = pretrained_model_config
        self.adapter_size = pretrained_model_config.adapter_size

        class AdapterConfig:
            project_hidden_size: int = self.config.hidden_size
            hidden_act: str = "gelu"
            adapter_size: int = self.adapter_size  # 64
            adapter_initializer_range: float = 0.0002
            is_decoder: bool = False
            attention_probs_dropout_prob: float = 0.1
            hidden_dropout_prob: float = 0.1
            hidden_size: int = self.adapter_size
            initializer_range: float = 0.02
            intermediate_size: int = 3072
            layer_norm_eps: float = 1e-05
            max_position_embeddings: int = 514
            num_attention_heads: int = 12
            num_hidden_layers: int = pretrained_model_config.adapter_transformer_layers
            num_labels: int = 2
            output_attentions: bool = False
            output_hidden_states: bool = False
            torchscript: bool = False
            type_vocab_size: int = 1
            vocab_size: int = 50265
            chunk_size_feed_forward: int = 0
            add_cross_attention: bool = False

        self.adapter_config = AdapterConfig
        self.adapter_skip_layers = pretrained_model_config.adapter_skip_layers
        self.adapter_list = pretrained_model_config.adapter_list
        self.adapter_num = len(self.adapter_list)
        self.adapter = nn.ModuleList([Adapter(self.adapter_config) for _ in range(self.adapter_num)])

    def forward(self, pretrained_model_outputs):
        outputs = pretrained_model_outputs
        sequence_output = outputs[0]
        hidden_states = outputs.hidden_states
        hidden_states_last = torch.zeros(sequence_output.size()).to(next(self.parameters()).device)
        adapter_hidden_states = []
        adapter_hidden_states_count = 0
        for i, adapter_module in enumerate(self.adapter):
            fusion_state = hidden_states[self.adapter_list[i]] + hidden_states_last
            hidden_states_last = adapter_module(fusion_state)
            adapter_hidden_states.append(hidden_states_last)
            adapter_hidden_states_count += 1
            if self.adapter_skip_layers >= 1:
                if adapter_hidden_states_count % self.adapter_skip_layers == 0:
                    hidden_states_last = hidden_states_last + adapter_hidden_states[
                        int(adapter_hidden_states_count / self.adapter_skip_layers)]
        return hidden_states_last


def populate_config(roberta_config):
    if not hasattr(roberta_config, "adapter_size"):
        setattr(roberta_config, "adapter_size", [0, 11, 23])
    if not hasattr(roberta_config, "adapter_list"):
        setattr(roberta_config, "adapter_list", 768)
    if not hasattr(roberta_config, "adapter_transformer_layers"):
        setattr(roberta_config, "adapter_transformer_layers", 2)
    if not hasattr(roberta_config, "adapter_skip_layers"):
        setattr(roberta_config, "adapter_skip_layers", 0)
    if not hasattr(roberta_config, "fusion_mode"):
        setattr(roberta_config, "fusion_mode", "concat")
    setattr(roberta_config, "architectures", ["KAdapterModel"])
    return roberta_config


class KAdapterModel(RobertaModel):
    def __init__(self, config):
        super(KAdapterModel, self).__init__(config)
        config = populate_config(config)
        self.config = config
        self.fac_adapter = AdapterModel(self.config)
        self.lin_adapter = AdapterModel(self.config)
        self.adapter_num = 0
        if self.fac_adapter is not None:
            self.adapter_num += 1
        if self.lin_adapter is not None:
            self.adapter_num += 1
        if self.config.fusion_mode == 'concat':
            if self.fac_adapter is not None:
                self.task_dense_fac = nn.Linear(self.config.hidden_size + self.config.hidden_size,
                                                self.config.hidden_size)
            if self.lin_adapter is not None:
                self.task_dense_lin = nn.Linear(self.config.hidden_size + self.config.hidden_size,
                                                self.config.hidden_size)
            self.task_dense = nn.Linear(self.config.hidden_size + self.config.hidden_size, self.config.hidden_size)

    def forward(
            self,
            input_ids=None,
            attention_mask=None,
            token_type_ids=None,
            position_ids=None,
            head_mask=None,
            inputs_embeds=None,
            encoder_hidden_states=None,
            encoder_attention_mask=None,
            past_key_values=None,
            use_cache=None,
            output_attentions=None,
            output_hidden_states=None,
            return_dict=None
    ):
        outputs = super(KAdapterModel, self).forward(input_ids,
                                                     attention_mask=attention_mask,
                                                     token_type_ids=token_type_ids,
                                                     position_ids=position_ids,
                                                     head_mask=head_mask,
                                                     inputs_embeds=inputs_embeds,
                                                     encoder_hidden_states=encoder_hidden_states,
                                                     encoder_attention_mask=encoder_attention_mask,
                                                     past_key_values=past_key_values,
                                                     use_cache=use_cache,
                                                     output_attentions=output_attentions,
                                                     output_hidden_states=True
                                                     )
        pretrained_model_last_hidden_states = outputs[0]  # original roberta output
        if self.fac_adapter is not None:
            fac_adapter_outputs = self.fac_adapter(outputs)
        if self.lin_adapter is not None:
            lin_adapter_outputs = self.lin_adapter(outputs)
        if self.config.fusion_mode == 'concat':
            combine_features = pretrained_model_last_hidden_states
            if self.fac_adapter is not None:
                fac_features = self.task_dense_fac(torch.cat([combine_features, fac_adapter_outputs], dim=2))
                task_features = fac_features
            if self.lin_adapter is not None:
                lin_features = self.task_dense_lin(torch.cat([combine_features, lin_adapter_outputs], dim=2))
                task_features = lin_features
            if (self.fac_adapter is not None) and (self.lin_adapter is not None):
                task_features = self.task_dense(torch.cat([fac_features, lin_features], dim=2))
        if not return_dict:
            return (task_features, outputs[1]) + outputs[1:]

        return BaseModelOutputWithPoolingAndCrossAttentions(
            last_hidden_state=task_features,
            pooler_output=outputs[1],
            past_key_values=outputs.past_key_values,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
            cross_attentions=outputs.cross_attentions,
        )

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_kadapter_weights()
            return super().from_pretrained(KADAPTER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class KAdapterForSequenceClassification(RobertaForSequenceClassification):
    _keys_to_ignore_on_load_missing = [r"position_ids"]

    def __init__(self, config):
        super().__init__(config)
        self.num_labels = config.num_labels
        self.config = config
        self.roberta = KAdapterModel(config)
        self.classifier = RobertaClassificationHead(config)
        self.post_init()

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, labels=None, label2id=None, **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        if pretrained_model_name_or_path is None:
            download_extract_kadapter_weights()
            return super().from_pretrained(KADAPTER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class KAdapterForTokenClassification(RobertaForTokenClassification):
    _keys_to_ignore_on_load_unexpected = [r"pooler"]
    _keys_to_ignore_on_load_missing = [r"position_ids"]

    def __init__(self, config):
        super().__init__(config)
        self.num_labels = config.num_labels
        self.roberta = KAdapterModel(config)
        classifier_dropout = (
            config.classifier_dropout if config.classifier_dropout is not None else config.hidden_dropout_prob
        )
        self.dropout = nn.Dropout(classifier_dropout)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)
        self.post_init()

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, labels=None, label2id=None, **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        if pretrained_model_name_or_path is None:
            download_extract_kadapter_weights()
            return super().from_pretrained(KADAPTER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class KAdapterForQuestionAnswering(RobertaForQuestionAnswering):
    _keys_to_ignore_on_load_unexpected = [r"pooler"]
    _keys_to_ignore_on_load_missing = [r"position_ids"]

    def __init__(self, config):
        super().__init__(config)
        self.num_labels = config.num_labels
        self.roberta = KAdapterModel(config)
        self.qa_outputs = nn.Linear(config.hidden_size, config.num_labels)
        self.post_init()

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_kadapter_weights()
            return super().from_pretrained(KADAPTER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class KAdapterForMultipleChoice(RobertaForMultipleChoice):
    _keys_to_ignore_on_load_missing = [r"position_ids"]

    def __init__(self, config):
        super().__init__(config)
        self.roberta = KAdapterModel(config)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, 1)
        self.post_init()

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_kadapter_weights()
            return super().from_pretrained(KADAPTER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


if __name__ == "__main__":
    second_model = KAdapterForMultipleChoice.from_pretrained("pretrained_kadapter")
