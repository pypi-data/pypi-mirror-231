# -*- coding: utf-8 -*-
"""
This module provides helper classes for training huggingface models using the interface in mangoes.modeling.finetuning.
These classes are mainly called internally from mangoes.modeling.finetuning, however they can be instantiated on
their own (or subclassed) and passed to training methods in mangoes.modeling.finetuning for more customization/control.
"""
import random
import inspect
import warnings
import transformers
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset
from mangoes.modeling.enhanced_models import ErnieTokenizer


def freeze_base_layers(model):
    """
    Function to freeze the base layer in a fine tuning/pretraining model
    """
    for param in model.base_model.parameters():
        param.requires_grad = False


class DataCollatorPossiblyWithExtraInputs(transformers.DataCollatorWithPadding):
    def __call__(self, features):
        batch = self.tokenizer.pad(
            features,
            padding=self.padding,
            max_length=self.max_length,
            pad_to_multiple_of=self.pad_to_multiple_of,
            return_tensors=self.return_tensors,
        )
        if "label" in batch:
            batch["labels"] = batch["label"]
            del batch["label"]
        if "label_ids" in batch:
            batch["labels"] = batch["label_ids"]
            del batch["label_ids"]
        return batch


class MangoesTextClassificationDataset(Dataset):
    """
    Subclass of torch.utils.data.Dataset class for sequence or token classification.
    To be used with transformers.Trainer.

    Parameters
    ----------
    texts: List[str] or List[List[str]]
        Input text sequences. Note that token classification, inputs must be pre-split to line up with token labels.
    labels: List[str or int] if seq classification, else List[List[str or int]] if token classification
        Labels can be raw strings, which will us label2id to convert to ids, or the ids themselves.
    tokenizer: transformers.Tokenizer
    max_len: int
        max length of input sequences, if None, will default to tokenizer.model_max_length
    label2id: dict of str -> int
        if labels are not already converted to output ids, dictionary with mapping to use.
    """

    def __init__(self, texts, labels, tokenizer, text_pairs=None, max_len=None, label2id=None, include_labels=True,
                 text_annotations=None, text_pair_annotations=None):
        self.tokenizer = tokenizer
        presplit_text = True if isinstance(texts[0], list) else False
        self.token_classes = False
        if include_labels:
            token_classes = True if isinstance(labels[0], list) else False
            if token_classes:
                # if token classification
                raw_labels = True if isinstance(labels[0][0], str) else False
                assert presplit_text, \
                    "Input sequences to MangoesTextClassificationDataset must be pre-split if token classification"
                if hasattr(self.tokenizer, "add_prefix_space"):
                    self.tokenizer.add_prefix_space = True
                if text_pairs is not None:
                    warnings.warn("Token classification with MangoesTextClassificationDataset currently doesn't "
                                  "support text pairs. Either consolidate prior to dataset creation or subclass.")
            else:
                # if sequence classification
                raw_labels = True if isinstance(labels[0], str) else False
            if raw_labels and label2id is None:
                raise TypeError(
                    'Labels passed to dataset are not converted into output ids and no id mapping was passed.')
            if raw_labels:
                if token_classes:
                    labels = [[label2id[label] for label in sublist] for sublist in labels]
                else:
                    labels = [label2id[label] for label in labels]
            self.token_classes = token_classes
            self.labels = labels
        self.max_len = max_len if max_len is not None else tokenizer.model_max_length
        self.input_dicts = []
        for i in range(len(texts)):
            if isinstance(self.tokenizer, ErnieTokenizer)and (
                    text_annotations is not None):
                encoding = self.tokenizer(
                    texts[i],
                    text_pair=None if text_pairs is None else text_pairs[i],
                    add_special_tokens=True,
                    max_length=self.max_len,
                    return_token_type_ids=False,
                    padding=True,
                    return_attention_mask=True,
                    return_tensors='pt',
                    truncation=True,
                    is_split_into_words=presplit_text,
                    text_annotations=text_annotations[i],
                    text_pair_annotations=text_pair_annotations[i] if
                    (text_pair_annotations is not None and text_pairs is not None) else None,
                )
            else:
                encoding = self.tokenizer(
                    texts[i],
                    text_pair=None if text_pairs is None else text_pairs[i],
                    add_special_tokens=True,
                    max_length=self.max_len,
                    return_token_type_ids=False,
                    padding=True,
                    return_attention_mask=True,
                    return_tensors='pt',
                    truncation=True,
                    is_split_into_words=presplit_text,
                )
            return_dict = {name: tensor.squeeze(0) for name, tensor in encoding.items() if name in
                           self.tokenizer.model_input_names}
            if include_labels:
                if self.token_classes:
                    if isinstance(self.tokenizer, transformers.PreTrainedTokenizerFast):
                        word_ids = encoding.word_ids()
                    else:
                        word_ids = self.get_word_ids(texts[i])
                    previous_word_idx = None
                    label_ids = []
                    for word_idx in word_ids:
                        if word_idx is None:
                            label_ids.append(-100)
                        elif word_idx >= len(texts[i]):
                            break
                        elif word_idx != previous_word_idx:  # Only label the first token of a given word.
                            label_ids.append(self.labels[i][word_idx])
                        else:
                            label_ids.append(-100)
                        previous_word_idx = word_idx
                    return_dict['labels'] = F.pad(torch.tensor(label_ids, dtype=torch.long),
                                                  [0, return_dict["input_ids"].shape[-1] - len(label_ids)], value=-100)
                else:
                    return_dict['labels'] = torch.tensor(self.labels[i],
                                                         dtype=torch.long if isinstance(self.labels[i],
                                                                                        int) else torch.float)
            self.input_dicts.append(return_dict)

    def get_word_ids(self, text):
        word_ids = [None]  # initialize with None for special token at the start
        for i, token in enumerate(text):
            sub_tokens = self.tokenizer.tokenize(token)
            for _ in sub_tokens:
                word_ids.append(i)
        word_ids.append(None)  # for end of sequence special token
        return word_ids

    def __len__(self):
        return len(self.input_dicts)

    def __getitem__(self, item):
        return self.input_dicts[item]


def update_input_spans(old_input_ids, new_input_ids, start_index, end_index):
    """
    Some enhanced models insert entity ids or other augmented ids into the input sequences. However, if predicting a
    span (coref, question answering tasks), this can change the span position. This function takes the original and new
    input id sequences and spans, and updates the spans if the new sequence contains inserted ids.

    :param old_input_ids: torch tensor of ids
    :param new_input_ids: torch tensor of possible augmented ids
    :param start_index: torch tensor containing start of span in input sequence
    :param end_index: torch tensor containing end of span in input sequence
    :return: (new_start_index, new_end_index
    """
    # list of tuples: first int is index in original sequence, 2nd is additional tokens in new sequence
    offsets = [(0, 0)]
    current_offset = 0
    for i in range(old_input_ids.shape[0]):
        new_offset = 0
        while not i + current_offset >= new_input_ids.shape[0] and \
                not old_input_ids[i] == new_input_ids[i + current_offset]:
            current_offset += 1
            new_offset += 1
        if new_offset > 0:
            offsets.append((i, new_offset))
    return start_index + sum(x[1] for x in offsets if x[0] <= start_index), \
           end_index + sum(x[1] for x in offsets if x[0] <= end_index)


class MangoesQuestionAnsweringDataset(Dataset):
    """
    Subclass of Torch Dataset for question answering datasets. Currently meant to work with BERT models.

    Parameters
    ----------
    tokenizer: transformers.Tokenizer
    question_texts: List of str
        The texts corresponding to the questions
    context_texts: List of str
        The texts corresponding to the contexts
    answer_texts: List of str
        The texts corresponding to the answers
    start_indices: List of int
        The character positions of the start of the answers
    max_seq_length:int
        The maximum total input sequence length after tokenization.
    doc_stride: int
        When splitting up a long document into chunks, how much stride to take between chunks.
    max_query_length: int
        The maximum number of tokens for the question.
    """

    def __init__(self, tokenizer, question_texts, context_texts, answer_texts, start_indices, max_seq_length=512,
                 doc_stride=128, max_query_length=64):
        if not len(question_texts) == len(answer_texts) or not len(question_texts) == len(start_indices) or \
                not len(question_texts) == len(context_texts):
            raise ValueError("Question Answering dataset needs answers, contexts, and start indices for every example")
        if max_seq_length > tokenizer.model_max_length:
            raise ValueError(
                "max_seq_length argument is greater than the max input sequence length for the pretrained model.")
        self.model_input_names = tokenizer.model_input_names
        examples = []
        for i in range(len(question_texts)):
            examples.append(transformers.SquadExample(qas_id=i, question_text=question_texts[i],
                                                      context_text=context_texts[i], answer_text=answer_texts[i],
                                                      start_position_character=start_indices[i], title=""))
        self.features = transformers.squad_convert_examples_to_features(examples, tokenizer,
                                                                        max_seq_length=max_seq_length,
                                                                        doc_stride=doc_stride,
                                                                        max_query_length=max_query_length,
                                                                        is_training=True)
        for i in range(len(self.features)):
            inputs = {
                name: torch.tensor(value, dtype=torch.long) for name, value in self.features[i].__dict__.items()
                if name in self.model_input_names
            }
            start_positions = torch.tensor(self.features[i].start_position, dtype=torch.long)
            end_positions = torch.tensor(self.features[i].end_position, dtype=torch.long)
            inputs.update({"start_positions": start_positions, "end_positions": end_positions})
            self.features[i] = inputs
        if not all(input_name in self.features[0] for input_name in self.model_input_names):
            for i in range(len(self.features)):
                input_text = tokenizer.decode(self.features[i]["input_ids"], clean_up_tokenization_spaces=True)
                input_seqs = input_text.split(tokenizer.sep_token)
                text = input_seqs[0].split()[1:]  # split on whitespace, skip first special token
                # some tokenizers (such as BART) use two sep tokens
                text_pair = input_seqs[1].split() if len(input_seqs[1]) > 0 else input_seqs[2].split()
                inputs = tokenizer(
                    text=text,
                    text_pair=text_pair,
                    padding="max_length",
                    truncation=None,
                    is_split_into_words=True,
                    max_length=tokenizer.model_max_length,
                    stride=doc_stride,
                    return_tensors="pt",
                    return_token_type_ids=True,
                    return_special_tokens_mask=False,
                    return_offsets_mapping=False,
                    return_overflowing_tokens=True
                )
                inputs = {k: v.squeeze(0) for k, v in inputs.items()}
                if not torch.equal(self.features[i]["input_ids"], inputs["input_ids"]):
                    new_start, new_end = update_input_spans(self.features[i]["input_ids"], inputs["input_ids"],
                                                            self.features[i]["start_positions"],
                                                            self.features[i]["end_positions"])
                    self.features[i]["start_positions"] = new_start
                    self.features[i]["end_positions"] = new_end
                self.features[i].update(inputs)

    def __len__(self):
        return len(self.features)

    def __getitem__(self, i):
        return self.features[i]


class QuestionAnsweringPipelinePossiblyWithEntities(transformers.QuestionAnsweringPipeline):
    def _forward(self, inputs):
        example = inputs["example"]  # SquadExample
        model_inputs = {k: inputs[k] for k in self.tokenizer.model_input_names if k in inputs}
        if not all(input_name in inputs for input_name in self.tokenizer.model_input_names):
            input_text = self.tokenizer.batch_decode(inputs["input_ids"], clean_up_tokenization_spaces=True)
            text = []
            text_pair = []
            for i in range(len(input_text)):
                input_seqs = input_text[i].split(self.tokenizer.sep_token)
                text.append(input_seqs[0].split()[1:])  # split on whitespace, skip first special token
                text_pair.append(input_seqs[1].split() if len(input_seqs[1]) > 0 else input_seqs[2].split())
            extra_inputs = self.tokenizer(
                text=text,
                text_pair=text_pair,
                padding="max_length",
                truncation=None,
                is_split_into_words=True,
                max_length=inputs["input_ids"].shape[-1],
                stride=min(inputs["input_ids"].shape[-1] // 2, 128),
                return_tensors="pt",
                return_token_type_ids=True,
                return_special_tokens_mask=False,
                return_offsets_mapping=False,
                return_overflowing_tokens=False
            )
            model_inputs.update(extra_inputs)
            for k, v in model_inputs.items():
                if v.dtype in (torch.float, torch.double):
                    model_inputs[k] = v.type(next(self.model.parameters()).dtype)
        start, end = self.model(**model_inputs)[:2]
        return {"start": start, "end": end, "example": example, **inputs}


class MangoesCoreferenceDataset(Dataset):
    """
    Subclass of Torch Dataset for co-reference datasets such as Ontonotes. Currently meant to work with BERT models.

    Each example is one document. Documents are parsed by first tokenizing each sentence then aggregating sentences into
    segments, keeping track of label, metadata, and sentence indices.

    Parameters
    ----------
    tokenizer: transformers.BertTokenizerFast
        tokenizer to use
    use_metadata: Boolean
        Whether or not to use speaker ids and genres
    max_segment_len: int
        maximum number of sub-tokens for one segment
    max_segments: int
        Maximum number of segments to return per __getitem__ (ie per document)
    documents: List of Lists of Lists of strings
        Text for each document. As cluster ids are labeled by word, a document is a list of sentences. One
        sentence is a list of words (ie already split on whitespace/punctuation)
    cluster_ids: List of Lists of Lists of (ints or Tuple(int, int))
        Cluster ids for each word in documents argument. Assumes words that aren't mentions have either None or -1 as
        id. In the case where a word belongs to two different spans (with different cluster ids), the cluster id for
        word should be a tuple of ints corresponding to the different cluster ids.
    speaker_ids: List of Lists of Lists of ints
        Speaker id for each word in documents. Assumes positive ids (special tokens (such as [CLS] and [SEP] that are
        added at beginning and end of segments) will be assigned speaker ids of -1)
    genres: List of ints or strings
        Genre (id) for each document. If strings, genre_to_id parameter needs to not be None
    genre_to_id: dict of string->int
        Mapping of genres to their id number.
    """

    def __init__(self, tokenizer, use_metadata, max_segment_len, max_segments, documents, cluster_ids, speaker_ids=None,
                 genres=None, genre_to_id=None):
        self.use_metadata = use_metadata
        if (use_metadata and speaker_ids is None) or (use_metadata and genres is None):
            raise RuntimeError("use_metadata argument is set to True in MangoesCoreferenceDataset init function, but "
                               "missing speaker and/or genre input data")
        if use_metadata and isinstance(genres[0], str) and not genre_to_id:
            raise RuntimeError("Input genre data has not been converted to ids yet, and genre_to_id parameter is "
                               "unfilled")
        self.examples = []
        self.max_segments = max_segments
        for i in range(len(documents)):
            if use_metadata:
                ids, attention_mask, sentence_map, gold_starts, gold_ends, clus_ids, speakers = \
                    make_coref_example(tokenizer, documents[i], cluster_ids[i], speaker_ids[i], use_metadata,
                                       max_segment_len)
            else:
                ids, attention_mask, sentence_map, gold_starts, gold_ends, clus_ids = \
                    make_coref_example(tokenizer, documents[i], cluster_ids[i], None, use_metadata,
                                       max_segment_len)
            self.examples.append([torch.as_tensor(ids), torch.as_tensor(attention_mask),
                                  torch.as_tensor(sentence_map), torch.as_tensor(gold_starts),
                                  torch.as_tensor(gold_ends), torch.as_tensor(clus_ids)])
            if use_metadata:
                self.examples[-1].append(torch.as_tensor(speakers))
                self.examples[-1].append(torch.as_tensor(genres[i] if isinstance(genres[i], int) else
                                                         genre_to_id[genres[i]]))
        if not all(
                input_name in {"input_ids", "attention_mask", "sentence_map", "gold_starts", "gold_ends", "cluster_ids"}
                for input_name in tokenizer.model_input_names):
            self.extra_inputs = []
            for i in range(len(documents)):
                input_text = tokenizer.batch_decode(self.examples[i][0], clean_up_tokenization_spaces=True)
                extra_inputs = tokenizer(
                    text=input_text,
                    text_pair=None,
                    padding="max_length",
                    truncation=True,
                    is_split_into_words=False,
                    max_length=self.examples[i][0].shape[-1],
                    return_tensors="pt",
                    return_token_type_ids=True,
                    return_special_tokens_mask=True,
                    return_offsets_mapping=False,
                    return_overflowing_tokens=False
                )
                extra_inputs = {k: extra_inputs[k] for k in tokenizer.model_input_names if
                                k not in {"input_ids", "attention_mask", "sentence_map", "gold_starts", "gold_ends",
                                          "cluster_ids"}}
                self.extra_inputs.append(extra_inputs)
        else:
            self.extra_inputs = None
        # self.examples: list of tensors in following order:
        #   ids, attentionmask, sentencemap, goldstarts, goldends, clusterids, speaker ids, genre

    @staticmethod
    def pad_list(values, target_length, pad_value=0):
        """
        Function to pad a list of values to a specific length, appending the pad_value to the end of the list.

        Parameters
        ----------
        values: List
        target_length: int
        pad_value: value pad the list with

        Returns
        -------
        list of values, padded to target length
        """
        while len(values) < target_length:
            values.append(pad_value)
        return values

    @staticmethod
    def get_subtoken_data(token_data, offset_mapping):
        """
        Function to map token data to sub tokens. For example, if a token is split into two sub-tokens,
        the cluster id (or speaker id) for the token needs to be associated with both sub-tokens.

        Parameters
        ----------
        token_data: cluster ids of tokens
        offset_mapping: for each sub-token, a (start index, end index) tuple of indices into it's original token
            As returned by a transformers.tokenizer if return_offsets_mapping=True.

        Returns
        -------
        List containing cluster ids for each token
        """
        token_index = -1
        sub_token_data = []
        for (start, _) in offset_mapping:
            if start == 0:
                token_index += 1
            sub_token_data.append(token_data[token_index])
        return sub_token_data

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, i):
        """
        Each example is 1 document that consists of the following:
        input_ids: tensor of size (num_segments, sequence_length)
            input token ids
        attention_mask: tensor of size (num_segments, sequence_length)
            attention mask of input segments
        sentence_map: tensor of size (num_tokens)
            sentence id for each input token in input document
        speaker_ids: tensor of size (num_segments, sequence_length)
            speaker ids for each token (only used if self.use_metadata is True)
        genre: tensor of size (1)
            genre id for document
        gold_starts: tensor of size (labeled)
            start token indices (in flattened document) of labeled spans
        gold_ends: tensor of size (labeled)
            end token indices (in flattened document) of labeled spans
        cluster_ids: tensor of size (labeled)
            cluster ids of each labeled span
        """
        if self.use_metadata:
            ids, attention_mask, sentence_map, gold_starts, gold_ends, cluster_ids, speaker_ids, genre = \
                self.examples[i]
        else:
            ids, attention_mask, sentence_map, gold_starts, gold_ends, cluster_ids = self.examples[i]

        if self.extra_inputs is not None:
            extra_inputs = self.extra_inputs[i]
        if len(ids) > self.max_segments:
            sentence_offset = random.randint(0, len(ids) - self.max_segments)
            token_offset = attention_mask[:sentence_offset].sum()
            ids = ids[sentence_offset:sentence_offset + self.max_segments]
            attention_mask = attention_mask[sentence_offset:sentence_offset + self.max_segments]
            num_tokens = attention_mask.sum()
            sentence_map = sentence_map[token_offset:token_offset + num_tokens]
            gold_spans = torch.logical_and(gold_ends >= token_offset, gold_starts < token_offset + num_tokens)
            gold_starts = gold_starts[gold_spans] - token_offset
            gold_ends = gold_ends[gold_spans] - token_offset
            cluster_ids = cluster_ids[gold_spans]
            if self.use_metadata:
                speaker_ids = speaker_ids[sentence_offset:sentence_offset + self.max_segments]
            if self.extra_inputs is not None:
                extra_inputs = {k: v[sentence_offset:sentence_offset + self.max_segments] for k, v in
                                extra_inputs.items()}
        inputs = {
            "input_ids": ids,
            "attention_mask": attention_mask,
            "sentence_map": sentence_map,
            "gold_starts": gold_starts,
            "gold_ends": gold_ends,
            "cluster_ids": cluster_ids
        }
        if self.use_metadata:
            inputs.update({"speaker_ids": speaker_ids, "genre": genre})
        if self.extra_inputs is not None:
            inputs.update(extra_inputs)
        return inputs


class DataCollatorForMultipleChoice:
    """
    Data collator that will dynamically pad the inputs for multiple choice received.
    """

    def __init__(self, tokenizer, padding=True, max_length=None, pad_to_multiple_of=None):
        self.tokenizer = tokenizer
        self.padding = padding
        self.max_length = max_length
        self.pad_to_multiple_of = pad_to_multiple_of

    def __call__(self, features):
        label_name = "label" if "label" in features[0].keys() else "labels"
        labels = [feature.pop(label_name) for feature in features]
        batch_size = len(features)
        num_choices = len(features[0]["input_ids"])
        flattened_features = [[{k: v[i] for k, v in feature.items()} for i in range(num_choices)] for feature in
                              features]
        flattened_features = sum(flattened_features, [])

        batch = self.tokenizer.pad(
            flattened_features,
            padding=self.padding,
            max_length=self.max_length,
            pad_to_multiple_of=self.pad_to_multiple_of,
            return_tensors="pt",
        )
        for k, v in batch.items():
            new_shape = (batch_size, num_choices) + tuple(int(x) for x in list(v.shape[1:]))
            batch[k] = v.view(new_shape)
        batch["labels"] = torch.tensor(labels, dtype=torch.int64)
        return batch


class MangoesMultipleChoiceDataset(Dataset):
    """
    Subclass of Torch Dataset for multiple choice datasets such as SWAG.

    For information on how multiple choice datasets are formatted using this class, see
    https://github.com/google-research/bert/issues/38

    And this link for explanation of Huggingface's multiple choice models:
    https://github.com/huggingface/transformers/issues/7701#issuecomment-707149546

    Parameters
    ----------
    tokenizer: transformer.tokenizer
        tokenizer to use
    question_texts: List of str
        The texts corresponding to the questions/contexts.
    choices_texts: List of str
        The texts corresponding to the answer choices
    labels: List of int
        The indices of the correct answers
    """

    def __init__(self, tokenizer, question_texts, choices_texts, labels):
        self.tokenizer = tokenizer
        self.labels = labels
        self.encoded_features = []
        for i in range(len(question_texts)):
            num_choices = len(choices_texts[i])
            questions = [question_texts[i]] * num_choices
            self.encoded_features.append(tokenizer(questions, choices_texts[i], truncation=True))

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, i):
        inputs = self.encoded_features[i]
        inputs["labels"] = torch.as_tensor(int(self.labels[i]))
        return inputs


class MultipleLearnRateFineTuneTrainer(transformers.Trainer):
    """
    Subclass of Huggingface Trainer to accept different learning rates for base model parameters and task specific
    parameters, in the context of a fine-tuning task.

    Parameters
    ---------
    task_learn_rate: float
        Learning rate to be used for task specific parameters, (base parameters will use the normal, ie already defined
        in args, learn rate)
    task_weight_decay: float
        Weight decay to be used for task specific parameters, (base parameters will use the normal, ie already defined
        in args, weight decay)
    base_keyword: str
        String to be used to differentiate base model and task specific parameters. All named parameters that have
        "base_keyword" somewhere in the name will be considered part of the base model, while all parameters that don't
        will be considered part of the task specific parameters.
    For documentation of the rest of the init parameters, see
        https://huggingface.co/transformers/main_classes/trainer.html#id1
    """

    def __init__(
            self,
            task_learn_rate,
            task_weight_decay,
            base_keyword="bert",
            model=None,
            args=None,
            data_collator=None,
            train_dataset=None,
            eval_dataset=None,
            tokenizer=None,
            model_init=None,
            compute_metrics=None,
            callbacks=None,
            optimizers=(None, None)
    ):
        self.task_learn_rate = task_learn_rate
        self.base_keyword = base_keyword
        self.task_weight_decay = task_weight_decay
        super(MultipleLearnRateFineTuneTrainer, self).__init__(model, args, data_collator, train_dataset, eval_dataset,
                                                               tokenizer, model_init, compute_metrics, callbacks,
                                                               optimizers)

    def create_optimizer_and_scheduler(self, num_training_steps):
        """
        Setup the optimizer and the learning rate scheduler.

        This will use AdamW. If you want to use something else (ie, a different optimizer and multiple learn rates), you
        can subclass and override this method in a subclass.
        """
        if self.optimizer is None:
            no_decay = ["bias", "LayerNorm.weight"]
            optimizer_grouped_parameters = [
                {
                    "params": [p for n, p in self.model.named_parameters() if not any(nd in n for nd in no_decay) and
                               self.base_keyword in n],
                    "weight_decay": self.args.weight_decay,
                },
                {
                    "params": [p for n, p in self.model.named_parameters() if any(nd in n for nd in no_decay) and
                               self.base_keyword in n],
                    "weight_decay": 0.0,
                },
                {
                    "params": [p for n, p in self.model.named_parameters() if not any(nd in n for nd in no_decay) and
                               self.base_keyword not in n],
                    "weight_decay": self.task_weight_decay,
                    "lr": self.task_learn_rate,
                },
                {
                    "params": [p for n, p in self.model.named_parameters() if any(nd in n for nd in no_decay) and
                               self.base_keyword not in n],
                    "weight_decay": 0.0,
                    "lr": self.task_learn_rate,
                },
            ]
            if self.args.adafactor:
                optimizer_cls = transformers.Adafactor
                optimizer_kwargs = {"scale_parameter": False, "relative_step": False}
            else:
                optimizer_cls = transformers.AdamW
                optimizer_kwargs = {
                    "betas": (self.args.adam_beta1, self.args.adam_beta2),
                    "eps": self.args.adam_epsilon,
                }
            optimizer_kwargs["lr"] = self.args.learning_rate
            self.optimizer = optimizer_cls(optimizer_grouped_parameters, **optimizer_kwargs)

        if self.lr_scheduler is None:
            self.lr_scheduler = transformers.get_scheduler(
                self.args.lr_scheduler_type,
                self.optimizer,
                num_warmup_steps=self.args.warmup_steps,
                num_training_steps=num_training_steps,
            )


class CoreferenceFineTuneTrainer(MultipleLearnRateFineTuneTrainer):
    """
    Subclass of the Mangoes MultipleLearnRateFineTuneTrainer that does not collate examples into batches, for use in the
    default Coreference Fine Tuning Trainer.

    This method introduces a dummy batch collation method, because the batches in the implemented fine tuning method
    (see paper below) are exactly 1 document each, and are pre-collated in the dataset class.
    This is based on the independent variant of the coreference resolution method described in
    https://arxiv.org/pdf/1908.09091.pdf.

    For documentation of the init parameters, see the documentation for MangoesMultipleLearnRateFineTuneTrainer
    """

    def __init__(
            self,
            task_learn_rate,
            task_weight_decay,
            base_keyword="bert",
            model=None,
            args=None,
            train_dataset=None,
            eval_dataset=None,
            tokenizer=None,
            model_init=None,
            compute_metrics=None,
            callbacks=None,
            optimizers=(None, None)
    ):
        def collate_fn(batch):
            return batch[0]

        super(CoreferenceFineTuneTrainer, self).__init__(task_learn_rate, task_weight_decay, base_keyword, model, args,
                                                         collate_fn, train_dataset, eval_dataset, tokenizer,
                                                         model_init, compute_metrics, callbacks, optimizers)

    def _set_signature_columns_if_needed(self):
        # used by trainer when finding which data columns to pass to train loop. Here we subclass and look at the
        # features_model signature too.
        if self._signature_columns is None:
            # Inspect model forward signature to keep only the arguments it accepts.
            signature = inspect.signature(self.model.forward)
            signature_base_model = inspect.signature(self.model.features_model.forward)
            self._signature_columns = list(
                set(signature.parameters.keys()).union(set(signature_base_model.parameters.keys())))
            # Labels may be named label or label_ids, the default data collator handles that.
            self._signature_columns += list(set(["label", "label_ids"] + self.label_names))


def make_coref_example(tokenizer, document, cluster_ids, speaker_ids, use_metadata, max_segment_len):
    """
    Function to do co-reference example preprocessing

    Parameters
    ----------
    tokenizer: transformers.PreTrainedTokenizerBase
        tokenizer to use
    use_metadata: Boolean
        Whether or not to use speaker ids and genres
    max_segment_len: int
        maximum number of sub-tokens for one segment
    document: Lists of Lists of strings
        list of sentences. One sentence is a list of words (ie already split on whitespace/punctuation)
    cluster_ids: Lists of Lists of (ints or Tuple(int, int))
        Cluster id for each word in document argument. Assumes words that aren't mentions have either None or -1 as
        id. In the case where a word belongs to two different spans (with different cluster ids), the cluster id for
        word should be a tuple of ints corresponding to the different cluster ids.
        This parameter is optional (can be used for inference)
    speaker_ids: Lists of Lists of ints
        Speaker id for each word in document. Assumes positive ids (special tokens (such as [CLS] and [SEP] that are
        added at beginning and end of segments) will be assigned speaker ids of -1)

    Returns:
    -------
    segments_ids: torch tensor
        token ids, broken into segments and padded to max_segment_len
    segments_attention_mask: torch tensor
        attention mask for segment ids
    sentence_map: torch tensor
         sentence id for each input token in input document
    gold_starts: torch tensor
        start token indices (in flattened document) of labeled spans. Only returned if cluster information is passed to
        function.
    gold_ends: torch tensor
        end token indices (in flattened document) of labeled spans. Only returned if cluster information is passed to
        function.
    cluster_ids: torch tensor
        cluster ids of each labeled span. Only returned if cluster information is passed to function.
    speaker_ids: torch tensor
        speaker ids for each token (only used if self.use_metadata is True)
    """
    # for each sentence, tokenize into word pieces then aggregate input ids, clusters, speakers
    subtoken_ids = []
    subtoken_cluster_ids = []
    subtoken_speakers = []
    subtoken_offset_mappings = []
    for j in range(len(document)):
        encoding = tokenizer(document[j], add_special_tokens=False, is_split_into_words=True,
                             return_offsets_mapping=False)
        offset_mapping = []
        for i, token in enumerate(document[j]):
            sub_tokens = tokenizer.tokenize(token)
            current_start = 0
            for sub_token in sub_tokens:
                offset_mapping.append((current_start, current_start + len(sub_token.replace("##", ""))))
                current_start = current_start + len(sub_token.replace("##", ""))
        encoding["offset_mapping"] = offset_mapping
        subtoken_ids.append(encoding["input_ids"])
        if cluster_ids is not None:
            subtoken_cluster_ids.append(MangoesCoreferenceDataset.get_subtoken_data(cluster_ids[j],
                                                                                    encoding["offset_mapping"]))
        subtoken_offset_mappings.append(encoding["offset_mapping"])
        if use_metadata and speaker_ids:
            subtoken_speakers.append(MangoesCoreferenceDataset.get_subtoken_data(speaker_ids[j],
                                                                                 encoding["offset_mapping"]))
    # aggregate into segments
    if cluster_ids is not None:
        assert len(subtoken_ids) == len(subtoken_cluster_ids)
    current_segment_ids = []
    current_segment_cluster_ids = []
    current_segment_speaker_ids = []
    current_sentence_map = []
    segments_ids = []
    segments_clusters = []
    segments_speakers = []
    segments_attention_mask = []
    sentence_map = []
    for j in range(len(subtoken_ids)):
        if len(current_segment_ids) + len(subtoken_ids[j]) <= max_segment_len - 2:
            current_segment_ids += subtoken_ids[j]
            if cluster_ids is not None:
                current_segment_cluster_ids += subtoken_cluster_ids[j]
            current_sentence_map += [j] * len(subtoken_ids[j])
            if use_metadata and speaker_ids:
                current_segment_speaker_ids += subtoken_speakers[j]
        else:
            if len(current_segment_ids) > 0:
                # segments contain cls and sep special tokens at beginning and end for BERT processing
                segments_ids.append(MangoesCoreferenceDataset.pad_list([tokenizer.cls_token_id] + current_segment_ids +
                                                                       [tokenizer.sep_token_id], max_segment_len,
                                                                       tokenizer.convert_tokens_to_ids(
                                                                           tokenizer.pad_token)))
                if cluster_ids is not None:
                    segments_clusters.append(
                        MangoesCoreferenceDataset.pad_list([None] + current_segment_cluster_ids + [None],
                                                           max_segment_len, None))
                segments_attention_mask.append(MangoesCoreferenceDataset.pad_list([1] * (len(current_segment_ids) + 2),
                                                                                  max_segment_len))
                sentence_map += [current_sentence_map[0]] + current_sentence_map + [current_sentence_map[-1] + 1]
                if use_metadata and speaker_ids:
                    segments_speakers.append(
                        MangoesCoreferenceDataset.pad_list([-1] + current_segment_speaker_ids + [-1],
                                                           max_segment_len))
            while len(subtoken_ids[j]) > max_segment_len - 2:
                # if sentence j is longer than max_seq_len, create segment out of as much as possible,
                # then remove these from sentence j and continue
                segment_stop_index = max_segment_len - 2
                while subtoken_offset_mappings[j][segment_stop_index - 1][0] > 0 or \
                        subtoken_offset_mappings[j][segment_stop_index][0] > 0:
                    # if breaking sentence in the middle of a token, truncate so whole token is in next segment
                    segment_stop_index -= 1
                segments_ids.append(MangoesCoreferenceDataset.pad_list([tokenizer.cls_token_id] +
                                                                       subtoken_ids[j][:segment_stop_index] +
                                                                       [tokenizer.sep_token_id], max_segment_len,
                                                                       tokenizer.convert_tokens_to_ids(
                                                                           tokenizer.pad_token)))
                if cluster_ids is not None:
                    segments_clusters.append(
                        MangoesCoreferenceDataset.pad_list([None] + subtoken_cluster_ids[j][:segment_stop_index]
                                                           + [None], max_segment_len, None))
                segments_attention_mask.append(
                    MangoesCoreferenceDataset.pad_list([1] * (segment_stop_index + 2), max_segment_len))
                sentence_map += ([j] * (segment_stop_index + 1)) + [j + 1]
                if use_metadata and speaker_ids:
                    segments_speakers.append(
                        MangoesCoreferenceDataset.pad_list([-1] + subtoken_speakers[j][:segment_stop_index] +
                                                           [-1], max_segment_len))
                # remove already added data
                subtoken_ids[j] = subtoken_ids[j][segment_stop_index:]
                if cluster_ids is not None:
                    subtoken_cluster_ids[j] = subtoken_cluster_ids[j][segment_stop_index:]
                if use_metadata and speaker_ids:
                    subtoken_speakers[j] = subtoken_speakers[j][segment_stop_index:]
            current_segment_ids = subtoken_ids[j]
            if cluster_ids is not None:
                current_segment_cluster_ids = subtoken_cluster_ids[j]
            current_sentence_map = [j] * len(subtoken_ids[j])
            if use_metadata and speaker_ids:
                current_segment_speaker_ids = subtoken_speakers[j]
    # get last segment
    segments_ids.append(MangoesCoreferenceDataset.pad_list([tokenizer.cls_token_id] + current_segment_ids +
                                                           [tokenizer.sep_token_id], max_segment_len,
                                                           tokenizer.convert_tokens_to_ids(tokenizer.pad_token)))

    segments_attention_mask.append(
        MangoesCoreferenceDataset.pad_list([1] * (len(current_segment_ids) + 2), max_segment_len))
    sentence_map += [current_sentence_map[0]] + current_sentence_map + [current_sentence_map[-1] + 1]

    if use_metadata:
        segments_speakers.append(MangoesCoreferenceDataset.pad_list([-1] + current_segment_speaker_ids + [-1],
                                                                    max_segment_len))
    if cluster_ids is None:
        if not use_metadata:
            return torch.as_tensor(segments_ids), torch.as_tensor(segments_attention_mask), \
                   torch.as_tensor(sentence_map),
        else:
            return torch.as_tensor(segments_ids), torch.as_tensor(segments_attention_mask), \
                   torch.as_tensor(sentence_map), torch.as_tensor(segments_speakers)
    segments_clusters.append(MangoesCoreferenceDataset.pad_list([None] + current_segment_cluster_ids + [None],
                                                                max_segment_len, None))
    # create document level info (cluster indices, cluster ids, sentence map, genre)
    gold_starts = []
    gold_ends = []
    gold_cluster_ids = []
    current_offset = 0
    for j in range(len(segments_clusters)):
        # loop over segments and create gold start/ends, ids
        valid_sub_tokens = sum(segments_attention_mask[j])
        cluster_sightings = {}  # keys: clusterids, values: all indices where that clusterid is observed
        for k in range(valid_sub_tokens):
            if segments_clusters[j][k]:
                if isinstance(segments_clusters[j][k], tuple) or isinstance(segments_clusters[j][k], list):
                    for clus_id in segments_clusters[j][k]:
                        if clus_id in cluster_sightings:
                            cluster_sightings[clus_id].append(k)
                        else:
                            cluster_sightings[clus_id] = [k]
                elif segments_clusters[j][k] >= 0:
                    if segments_clusters[j][k] in cluster_sightings:
                        cluster_sightings[segments_clusters[j][k]].append(k)
                    else:
                        cluster_sightings[segments_clusters[j][k]] = [k]
        for clus_id, indices in cluster_sightings.items():
            indices_pointer = 0
            while indices_pointer < len(indices):
                gold_starts.append(indices[indices_pointer] + current_offset)
                gold_cluster_ids.append(clus_id)
                while indices_pointer < len(indices) - 1 and indices[indices_pointer] == \
                        indices[indices_pointer + 1] - 1:
                    indices_pointer += 1
                gold_ends.append(indices[indices_pointer] + current_offset)
                indices_pointer += 1
        current_offset += valid_sub_tokens
    # sort cluster data by cluster start
    cluster_data = sorted(zip(gold_starts, gold_ends, gold_cluster_ids), key=lambda x: (x[0], x[1]))
    cluster_data = [list(t) for t in zip(*cluster_data)]
    if len(cluster_data) == 0:
        cluster_data = [[], [], []]
    if use_metadata:
        return torch.as_tensor(segments_ids), torch.as_tensor(segments_attention_mask), torch.as_tensor(sentence_map), \
               torch.as_tensor(cluster_data[0]), torch.as_tensor(cluster_data[1]), torch.as_tensor(cluster_data[2]), \
               torch.as_tensor(segments_speakers)
    return torch.as_tensor(segments_ids), torch.as_tensor(segments_attention_mask), torch.as_tensor(
        sentence_map), torch.as_tensor(cluster_data[0]), torch.as_tensor(cluster_data[1]), torch.as_tensor(
        cluster_data[2]),
