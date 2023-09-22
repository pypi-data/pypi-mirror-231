# -*- coding: utf-8 -*-
"""
This module provides an interface into the transformers pretrained models for fine tuning.
Note that for each fine-tuning class, any eligible model may be fine-tuned. See links in each class documentation for
list of eligible models.
"""
import warnings
import os

import transformers
from transformers.modeling_utils import load_state_dict
import torch
import torch.nn.functional as F

from mangoes.modeling.training_utils import MangoesTextClassificationDataset, MangoesQuestionAnsweringDataset, \
    CoreferenceFineTuneTrainer, MangoesCoreferenceDataset, MangoesMultipleChoiceDataset, \
    MultipleLearnRateFineTuneTrainer, freeze_base_layers, make_coref_example, DataCollatorForMultipleChoice, \
    QuestionAnsweringPipelinePossiblyWithEntities
from mangoes.modeling.transformer_base import PipelineMixin, TransformerModel
from mangoes.modeling.coref import TransformerModelForCoreferenceResolutionBase
from mangoes.modeling.enhanced_models import ErnieTokenizer, ErnieModel, KAdapterModel


class TransformerForFeatureExtraction(PipelineMixin, TransformerModel):
    """Class for using a pretrained transformer model and tokenizer. As it uses AutoModel (and not
    AutoModelForQuestionAnswering, for example), it can only be used for base pretrained models, and not fine tuning
    tasks.

    Parameters
    ----------
    pretrained_model: str, transformers.PretrainedModel subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated transformer model, either an transformers.AutoModel compatible class or a mangoes
              enhanced language model.
    pretrained_tokenizer: str, transformers.PreTrainedTokenizerBase subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated tokenizer, either an transformers.AutoTokenizer compatible class or a mangoes
              enhanced language model tokenizer.
    device: int, optional, defaults to None
        if -1, use cpu, if >= 0, use CUDA device number. If None, will use GPU if available
    **keyword_args include arguments passed to transformers.AutoConfig

    """

    def __init__(self, pretrained_model, pretrained_tokenizer, device=None, **keyword_args):
        PipelineMixin.__init__(self)
        TransformerModel.__init__(self, pretrained_model, pretrained_tokenizer, transformers.AutoModel, device=device,
                                  **keyword_args)
        if self.tokenizer.pad_token is None:  # to allow padding
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.config.pad_token_id = self.model.config.eos_token_id

    def _construct_pipeline(self):
        """
        Implementation for creating inference pipeline.
        """
        self.model.eval()
        self.pipeline = transformers.FeatureExtractionPipeline(self.model, self.tokenizer,
                                                               device=-1 if self.model.device.type == "cpu" else
                                                               self.model.device.index)

    def predict(self, inputs, **kwargs):
        """
        Run input text through the feature extraction pipeline, extracting the hidden states of each layer.

        Parameters
        ----------
        inputs: str or list of strs
            inputs to extract features

        Returns
        -------
        nested list of float, hidden states.
        """
        return self._predict(inputs, **kwargs)

    def train(self, output_dir=None, train_dataset=None, eval_dataset=None, collator=None, trainer=None,
              **training_args):
        """
        This function does nothing, use a task specific class to pre-train or fine-tune
        """
        warnings.warn("This base model class does not implement training, it is meant for feature extraction")


class TransformerForSequenceClassification(PipelineMixin, TransformerModel):
    """
    Transformers model with Sequence classification head (linear layer on top of pooled output).
    For a list of eligible model classes, see:
    https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForSequenceClassification.from_config.config

    :var self.tokenizer: transformers.AutoTokenizerFast object,
        see https://huggingface.co/docs/transformers/model_doc/auto for more documentation
    :var self.model: transformers.AutoForSequenceClassification object,
        see https://huggingface.co/docs/transformers/model_doc/auto

    Parameters
    ----------
    pretrained_model: str, transformers.PretrainedModel subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated transformer model, either an transformers.AutoModelForSequenceClassification
              compatible class or a mangoes enhanced language model.
    pretrained_tokenizer: str, transformers.PreTrainedTokenizerBase subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated tokenizer, either an transformers.AutoTokenizer compatible class or a mangoes
              enhanced language model tokenizer.
    labels: list of str
        List of class names. Will raise error if labels=None and label2id=None
    label2id: dict of str -> int
        dict mapping class name to index of output layer
        if None, will create from labels.
    device: int, optional, defaults to None
        if -1, use cpu, if >= 0, use CUDA device number. If None, will use GPU if available
    **keyword_args include arguments passed to transformers.AutoConfig
    """

    def __init__(self, pretrained_model, pretrained_tokenizer, labels=None, label2id=None, device=None,
                 **keyword_args):
        PipelineMixin.__init__(self)
        if label2id is None and labels is None and (not isinstance(pretrained_model, transformers.PreTrainedModel) or
                                                    pretrained_model.config.id2label is None):
            raise RuntimeError("Must provide either labels or label to id mapping, or pretrained_model has id2label "
                               "already set in config")
        if label2id is None:
            if labels is None:
                self.label2id = pretrained_model.config.id2label
            else:
                self.label2id = {tag: id for id, tag in enumerate(set(labels))}
        else:
            self.label2id = label2id
        self.id2label = {id: tag for tag, id in self.label2id.items()}
        keyword_args["id2label"] = self.id2label
        TransformerModel.__init__(self, pretrained_model, pretrained_tokenizer,
                                  transformers.AutoModelForSequenceClassification, device, **keyword_args)
        if self.tokenizer.pad_token is None:  # to allow batching during training, need to be able to pad
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.config.pad_token_id = self.model.config.eos_token_id

    def _construct_pipeline(self):
        """
        Implementation for creating inference pipeline.
        """
        self.model.eval()
        self.pipeline = transformers.TextClassificationPipeline(model=self.model, tokenizer=self.tokenizer,
                                                                device=-1 if self.model.device.type == "cpu" else
                                                                self.model.device.index)

    def predict(self, inputs, return_all_scores=False):
        """
        Predicts classes for input texts.

        Parameters
        ----------
        inputs: str or list of strs
            inputs to classify
        return_all_scores: Boolean (default=False)
            Whether to return all scores or just the predicted class score

        Returns
        -------
        list of dict, or list of list of dict if return_all_scores=True
        If one sequence is passed as input, a list with one element (either a dict or list of dicts if
            return_all_scores=True) will be returned.
        for each input, a dict containing:
            label (str) – The label predicted.
            score (float) – The corresponding probability.
        if return_all_scores, dict will be returned for each class, for each input
        """
        return self._predict(inputs, return_all_scores=return_all_scores)

    def train(self, output_dir=None, train_text=None, train_targets=None, eval_text=None, eval_targets=None,
              max_len=None, freeze_base=False, task_learn_rate=None, collator=None, train_dataset=None,
              eval_dataset=None, compute_metrics=None, trainer=None, **training_args):
        """
        Fine tune a transformer model on a text classification dataset

        Parameters
        ----------
        output_dir: str
            Path to the output directory where the model predictions and checkpoints will be written. Used to
            instantiate Trainer if trainer argument is None.
        train_text: List[str]
            list of training texts
        train_targets: List[int] or List [str]
            corresponding list of classes for each training text. If strings, will use label2id to convert to output
            indices, else will assume already converted.
        eval_text: (Optional) str or List[str]
            list of evaluation texts
        eval_targets: List[int]
            corresponding list of classes for each evaluation text
        max_len: int
            max length of input sequence. Will default to self.tokenizer.max_length() if None
        freeze_base: Boolean
            Whether to freeze the weights of the base model, so training only changes the task head weights.
            If true, the requires_grad flag for parameters of the base model will be set to false before training.
        task_learn_rate: float
            Learning rate to be used for task specific parameters, (base parameters will use the normal, ie already
            defined in **training_args, learning rate). If None, all parameters will use the same normal learning rate.
        collator: Transformers.DataCollator
            custom collator to use
        train_dataset, eval_dataset: torch.Dataset
            instantiated custom dataset object
        compute_metrics: function
            The function that will be used to compute metrics at evaluation. Must return a dictionary string to metric
            values. Used by the trainer, see https://huggingface.co/transformers/training.html#trainer for more info.
        trainer: Transformers.Trainer
            custom instantiated trainer to use
        training_args:
            keyword arguments for training. For complete list, see
            https://huggingface.co/transformers/main_classes/trainer.html#transformers.TrainingArguments
        """
        if freeze_base:
            freeze_base_layers(self.model)
        if trainer is None:
            if self.model_device.type == "cpu":
                training_args["no_cuda"] = True
            if output_dir is None:
                raise RuntimeError("Must provide output directory argument to train() method if trainer argument is "
                                   "None")
            if train_dataset is None:
                if train_text is None or train_targets is None:
                    raise RuntimeError("Incomplete training data provided to train method")
                train_dataset = MangoesTextClassificationDataset(train_text, train_targets, self.tokenizer,
                                                                 max_len=max_len, label2id=self.label2id)
            if eval_text is not None and eval_targets is not None and eval_dataset is None:
                eval_dataset = MangoesTextClassificationDataset(eval_text, eval_targets, self.tokenizer,
                                                                max_len=max_len, label2id=self.label2id)
            elif (eval_text is not None or eval_targets is not None) and eval_dataset is None:
                warnings.warn("Incomplete evaluation dataset provided to train(). Please include both texts and "
                              "targets. Skipping evaluation dataset.")
            if eval_dataset is not None and "evaluation_strategy" not in training_args:
                training_args["evaluation_strategy"] = "epoch"
            train_args = transformers.TrainingArguments(output_dir=output_dir, **training_args)
            if task_learn_rate is not None:
                trainer = MultipleLearnRateFineTuneTrainer(task_learn_rate=task_learn_rate,
                                                           task_weight_decay=train_args.weight_decay,
                                                           model=self.model, args=train_args,
                                                           train_dataset=train_dataset,
                                                           data_collator=collator, eval_dataset=eval_dataset,
                                                           tokenizer=self.tokenizer, compute_metrics=compute_metrics)
            else:
                trainer = transformers.Trainer(self.model, args=train_args, train_dataset=train_dataset,
                                               data_collator=collator, eval_dataset=eval_dataset,
                                               tokenizer=self.tokenizer, compute_metrics=compute_metrics)
        self.trainer = trainer
        self.trainer.train()
        self.model.eval()


class TransformerForTokenClassification(PipelineMixin, TransformerModel):
    """
    Transformer model with Token classification head.
    For a list of eligible model classes, see:
    https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForTokenClassification.from_config.config

    :var self.tokenizer: transformers.AutoTokenizerFast object,
        see https://huggingface.co/docs/transformers/model_doc/auto for more documentation
    :var self.model: transformers.AutoModelForTokenClassification object,
        see https://huggingface.co/docs/transformers/model_doc/auto

    Parameters
    ----------
    pretrained_model: str, transformers.PretrainedModel subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated transformer model, either an transformers.AutoModelForTokenClassification
              compatible class or a mangoes enhanced language model.
    pretrained_tokenizer: str, transformers.PreTrainedTokenizerBase subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated tokenizer, either an transformers.AutoTokenizer compatible class or a mangoes
              enhanced language model tokenizer.
    labels: list of str
        list of class names. Will raise error if labels=None and label2id=None.
    label2id: dict of str -> int
        dict mapping class name to index of output layer
        if None, will create from labels.
    device: int, optional, defaults to None
        if -1, use cpu, if >= 0, use CUDA device number. If None, will use GPU if available
    **keyword_args include arguments passed to transformers.AutoConfig
    """

    def __init__(self, pretrained_model, pretrained_tokenizer, labels=None, label2id=None, device=None,
                 **keyword_args):
        PipelineMixin.__init__(self)
        if label2id is None and labels is None and (not isinstance(pretrained_model, transformers.PreTrainedModel) or
                                                    pretrained_model.config.id2label is None):
            raise RuntimeError("Must provide either labels or label to id mapping, or pretrained_model has id2label "
                               "already set in config")
        if label2id is None:
            if labels is None:
                self.label2id = pretrained_model.config.id2label
            else:
                self.label2id = {tag: id for id, tag in enumerate(set(labels))}
        else:
            self.label2id = label2id
        self.id2label = {id: tag for tag, id in self.label2id.items()}
        keyword_args["id2label"] = self.id2label
        TransformerModel.__init__(self, pretrained_model, pretrained_tokenizer,
                                  transformers.AutoModelForTokenClassification, device, **keyword_args)
        if self.tokenizer.pad_token is None:  # to allow batching during training, need to be able to pad
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.config.pad_token_id = self.model.config.eos_token_id

    def _construct_pipeline(self):
        """
        Implementation for creating inference pipeline.
        """
        self.model.eval()
        self.pipeline = transformers.TokenClassificationPipeline(model=self.model, tokenizer=self.tokenizer,
                                                                 device=-1 if self.model.device.type == "cpu" else
                                                                 self.model.device.index)

    def predict(self, inputs):
        """
        Predicts classes for input texts

        Parameters
        ----------
        inputs: str or list of strs
            inputs to classify

        Returns
        -------
        list of list of dict. For each sequence, a list of token prediction dicts. If a single sequence is passed as
        input, the output will be a list of 1 list of dictionaries.
        for each token, a dict containing:
            word (str) – The token/word classified.
            score (float) – The corresponding probability for entity.
            entity (str) – The entity predicted for that token/word.
            index (int, only present when self.grouped_entities=False) – The index of the corresponding token in the
                sentence.
        """
        prediction = self._predict(inputs)
        if isinstance(inputs, str):
            return [prediction]
        return prediction

    def train(self, output_dir=None, train_text=None, train_targets=None, eval_text=None, eval_targets=None,
              max_len=None, freeze_base=False, task_learn_rate=None, collator=None, train_dataset=None,
              eval_dataset=None, compute_metrics=None, trainer=None, **training_args):
        """
        Fine tune a transformers model on a text classification dataset

        Parameters
        ----------
        output_dir: str
            Path to the output directory where the model predictions and checkpoints will be written. Used to
            instantiate Trainer if trainer argument is None.
        train_text: List[str]
            list of training texts
        train_targets: List[List[int]]
            corresponding list of classes for each token in each training text
        eval_text: str or List[str]
            list of evaluation texts
        eval_targets: List[int]
            corresponding list of classes for each evaluation text
        max_len: int
            max length of input sequence. Will default to self.tokenizer.max_length() if None
        freeze_base: Boolean
            Whether to freeze the weights of the base model, so training only changes the task head weights.
            If true, the requires_grad flag for parameters of the base model will be set to false before training.
        task_learn_rate: float
            Learning rate to be used for task specific parameters, (base parameters will use the normal, ie already
            defined in **training_args, learning rate). If None, all parameters will use the same normal learning rate.
        collator: Transformers.DataCollator
            custom collator to use. If none, will use transformers.DataCollatorForTokenClassification.
        train_dataset, eval_dataset: torch.Dataset
            instantiated custom dataset object
        compute_metrics: function
            The function that will be used to compute metrics at evaluation. Must return a dictionary string to metric
            values. Used by the trainer, see https://huggingface.co/transformers/training.html#trainer for more info.
        trainer: Transformers.Trainer
            custom instantiated trainer to use
        training_args:
            keyword arguments for training. For complete list, see
            https://huggingface.co/transformers/main_classes/trainer.html#transformers.TrainingArguments
        """
        if freeze_base:
            freeze_base_layers(self.model)
        # TODO: allow token classification of tokens outside of pretrained tokenizer's vocabulary.
        # see https://huggingface.co/transformers/custom_datasets.html#token-classification-with-w-nut-emerging-entities
        if trainer is None:
            if self.model_device.type == "cpu":
                training_args["no_cuda"] = True
            if output_dir is None:
                raise RuntimeError("Must provide output directory argument to train() method if trainer argument is "
                                   "None")
            if train_dataset is None:
                if train_text is None or train_targets is None:
                    raise RuntimeError("Incomplete training data provided to train method")
                train_dataset = MangoesTextClassificationDataset(train_text, train_targets, self.tokenizer,
                                                                 max_len=max_len, label2id=self.label2id)
            if eval_text is not None and eval_targets is not None and eval_dataset is not None:
                eval_dataset = MangoesTextClassificationDataset(eval_text, eval_targets, self.tokenizer,
                                                                max_len=max_len, label2id=self.label2id)
            elif (eval_text is not None or eval_targets is not None) and eval_dataset is not None:
                warnings.warn("Incomplete evaluation dataset provided to train(). Please include both texts and "
                              "targets. Skipping evaluation dataset.")
            if eval_dataset is not None and "evaluation_strategy" not in training_args:
                training_args["evaluation_strategy"] = "epoch"
            train_args = transformers.TrainingArguments(output_dir=output_dir, **training_args)
            if collator is None:
                collator = transformers.DataCollatorForTokenClassification(self.tokenizer)
            if task_learn_rate is not None:
                trainer = MultipleLearnRateFineTuneTrainer(task_learn_rate=task_learn_rate,
                                                           task_weight_decay=train_args.weight_decay,
                                                           model=self.model, args=train_args,
                                                           train_dataset=train_dataset,
                                                           data_collator=collator, eval_dataset=eval_dataset,
                                                           tokenizer=self.tokenizer, compute_metrics=compute_metrics)
            else:
                trainer = transformers.Trainer(self.model, args=train_args, train_dataset=train_dataset,
                                               data_collator=collator, eval_dataset=eval_dataset,
                                               tokenizer=self.tokenizer, compute_metrics=compute_metrics)
        self.trainer = trainer
        self.trainer.train()
        self.model.eval()


class TransformerForQuestionAnswering(PipelineMixin, TransformerModel):
    """
    Transformer model with span classification head on top for extractive question-answering tasks like SQuAD (a linear
    layer on top of the hidden-states output to compute span start logits and span end logits).
    For a list of eligible model classes, see:
    https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForQuestionAnswering.from_config.config


    :var self.tokenizer: transformers.AutoTokenizerFast object,
        see https://huggingface.co/docs/transformers/model_doc/auto for more documentation
    :var self.model: transformers.AutoModelForQuestionAnswering object,
        see https://huggingface.co/docs/transformers/model_doc/auto

    Parameters
    ----------
    pretrained_model: str, transformers.PretrainedModel subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated transformer model, either an transformers.AutoModelForQuestionAnswering
              compatible class or a mangoes enhanced language model.
    pretrained_tokenizer: str, transformers.PreTrainedTokenizerBase subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated tokenizer, either an transformers.AutoTokenizer compatible class or a mangoes
              enhanced language model tokenizer.
    device: int, optional, defaults to None
        if -1, use cpu, if >= 0, use CUDA device number. If None, will use GPU if available
    **keyword_args include arguments passed to transformers.AutoConfig
    """

    def __init__(self, pretrained_model, pretrained_tokenizer, device=None, **keyword_args):
        PipelineMixin.__init__(self)
        self.tokenizer_name = pretrained_tokenizer
        # j.r.: (05/04/2020) currently the FastTokenizers don't work with QAPiplines, so we don't use fast tokenizer
        # https://github.com/huggingface/transformers/issues/7735
        # https://github.com/huggingface/transformers/issues/8787#issuecomment-779213050
        TransformerModel.__init__(self, pretrained_model, pretrained_tokenizer,
                                  transformers.AutoModelForQuestionAnswering, use_fast_tokenizer=False, device=device,
                                  **keyword_args)
        if self.tokenizer.pad_token is None:  # to allow batching during training, need to be able to pad
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.config.pad_token_id = self.model.config.eos_token_id

    def generate_outputs(self, question, context, pre_tokenized=False, output_attentions=False,
                         output_hidden_states=False, word_embeddings=False, doc_stride=128, **tokenizer_inputs):
        """
        Tokenize questions and context and pass them through the transformer model and QA head,
        optionally outputting hidden states or attention matrices.
        Works for single question/context or batch. If a single question/context is given, a batch of size 1 will be
        created.
        Note that offset_mappings are not returned for this class method: only tokenizers that inherit from
        transformers.PreTrainedTokenizerFast have this functionality, and these tokenizers are not compatible with
        QuestionAnswering functionality (see https://github.com/huggingface/transformers/issues/7735, and
        https://github.com/huggingface/transformers/issues/8787#issuecomment-779213050 for more details).

        Parameters
        ----------
        question: str or List[str] if pre_tokenized=False, else List[str] or List[List[str]]
            The question text
        context: str or List[str] if pre_tokenized=False, else List[str] or List[List[str]]
            The context text
        pre_tokenized: Boolean
            Whether or not the input text is pretokenized (ie, split on spaces)
        output_attentions: Boolean, optional, defaults to False
            Whether or not to return the attentions tensors of all attention layers.
        output_hidden_states: Boolean, optional, defaults to False
            Whether or not to return the hidden states of all layers.
        word_embeddings: Boolean
            Whether or not to filter special token embeddings and average subword embeddings (hidden states) into word
            embeddings. This functionality is not available for this task class. Use the feature extraction class
            instead.
        doc_stride: int, defaults to 128
             If the context is too long to fit with the question for the model, it will be split in several chunks with
             some overlap. This argument controls the size of that overlap.
        tokenizer_inputs: tokenizer_inputs include arguments passed to tokenizer, such as presaved entity annotations
            for enhanced models.

        Returns
        -------
        Dict containing (note that if single text sequence is pass as input, batch size will be 1):
        start_logits: torch.FloatTensor of shape (batch_size, sequence_length)
            Span-start scores (before SoftMax).
        end_logits: torch.FloatTensor of shape (batch_size, sequence_length)
            Span-end scores (before SoftMax).
        offset_mappings: Tensor of shape (batch_size, sequence_length, 2)
            Note that unlike other fine tuning classes and the base class, *offset mappings are not returned* for this
            class. See the class documentation for more details.
        hidden_states: Tuple (one for each layer) of torch.FloatTensor (batch_size, sequence_length, hidden_size).
            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
            Only returned if output_hidden_states is True
        attentions: Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length,
            sequence_length).
            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
            Only returned if output_attentions is True
        """
        question_first = bool(self.tokenizer.padding_side == "right")
        if (isinstance(question, str) or (isinstance(question[0], str) and pre_tokenized)) and \
                (isinstance(context, str) or (isinstance(context[0], str) and pre_tokenized)):
            # if single question and context
            question = [question]
            context = [context]
        elif isinstance(question, list) and (isinstance(context, str) or (isinstance(context[0], str) and
                                                                          pre_tokenized)):
            # if one context for multiple questions
            context = [context for _ in range(len(question))]
        elif isinstance(question, list) and isinstance(context, list) and len(question) != len(context):
            raise RuntimeError("Questions and contexts don't have the same lengths")

        inputs = self.tokenizer(
            text=question if question_first else context,
            text_pair=context if question_first else question,
            padding=True,
            truncation="only_second" if question_first else "only_first",
            is_split_into_words=pre_tokenized,
            max_length=self.tokenizer.model_max_length,
            stride=doc_stride,
            return_tensors="pt",
            return_token_type_ids=True,
            return_special_tokens_mask=True,
            return_offsets_mapping=False,
            return_overflowing_tokens=True,
            **tokenizer_inputs
        )
        inputs = {name: tensor for name, tensor in inputs.items() if name in self.tokenizer.model_input_names}
        self.model.eval()
        if word_embeddings:
            warnings.warn("Word embedding consolidation not available for Question Answering model. Consider using the"
                          "mangoes.modeling.TransformerForFeatureExtraction class for feature "
                          "extractions")
        with torch.no_grad():
            if self.model_device.type == "cuda":
                inputs = {name: tensor.to(self.model_device) for name, tensor in inputs.items()}
            results = self.model.forward(**inputs, return_dict=True,
                                         output_attentions=output_attentions,
                                         output_hidden_states=output_hidden_states)
        return dict(results)

    def _construct_pipeline(self):
        """
        Implementation for creating inference pipeline.
        """
        self.model.eval()
        self.pipeline = QuestionAnsweringPipelinePossiblyWithEntities(model=self.model, tokenizer=self.tokenizer,
                                                                      device=-1 if self.model.device.type == "cpu" else
                                                                      self.model.device.index)

    def predict(self, inputs=None, question=None, context=None, **kwargs):
        """
        Answer the question(s) given as inputs by using the context(s).
        Takes either transformers.SquadExample (or list of them) or lists of strings, see argument documentation.

        Parameters
        ----------
        inputs: transformers.SquadExample or a list of SquadExample
            One or several SquadExample containing the question and context.
        question: str or List[str]
            One or several question(s) (must be used in conjunction with the context argument).
        context: str or List[str]
            One or several context(s) associated with the question(s) (must be used in conjunction with the question
            argument).
        kwargs include:
        topk: int, defaults to 1
            The number of answers to return (will be chosen by order of likelihood).
        doc_stride: int, defaults to 128
            If the context is too long to fit with the question for the model, it will be split in several chunks with
            some overlap. This argument controls the size of that overlap.
        max_answer_len: int, defaults to 15
            The maximum length of predicted answers (e.g., only answers with a shorter length are considered).
        max_seq_len: int, defaults to 384
            The maximum length of the total sentence (context + question) after tokenization. The context will be split
            in several chunks (using doc_stride) if needed.
        max_question_len: int, defaults to 64
            The maximum length of the question after tokenization. It will be truncated if needed.
        handle_impossible_answer: bool, defaults to False
            Whether or not we accept impossible as an answer.

        Returns
        -------
        Returns a list of answers, one for each question. If only one question has been passed as input, returns a list
        with one dictionary.
        Each answer is a dict with:
        score: float
            The probability associated to the answer.
        start: int
            The start index of the answer (in the tokenized version of the input).
        end: int
            The end index of the answer (in the tokenized version of the input).
        answer: str
            The answer to the question.
        """
        if inputs is not None:
            prediction = self._predict(None, data=[inputs] if isinstance(inputs, transformers.SquadExample) else inputs,
                                       **kwargs)
        elif question is not None and context is not None:
            prediction = self._predict(None, question=question, context=context, **kwargs)
        else:
            raise RuntimeError("Must provide either SquadExample or both question and context to predict function.")
        if not isinstance(prediction, list):
            prediction = [prediction]
        return prediction

    def train(self, output_dir=None, train_question_texts=None, eval_question_texts=None, train_context_texts=None,
              eval_context_texts=None, train_answer_texts=None, eval_answer_texts=None, train_start_indices=None,
              eval_start_indices=None, max_seq_length=384, doc_stride=128, max_query_length=64, freeze_base=False,
              task_learn_rate=None, collator=None, train_dataset=None, eval_dataset=None, compute_metrics=None,
              trainer=None, **training_args):
        """
        Fine tune a transformers model on a question answering dataset

        Parameters
        ----------
        output_dir: str
            Path to the output directory where the model predictions and checkpoints will be written. Used to
            instantiate Trainer if trainer argument is None.
        train_question_texts, eval_question_texts: list of str
            The texts corresponding to the questions
        train_context_texts, eval_context_texts: list of str
            The texts corresponding to the contexts
        train_answer_texts, eval_answer_texts: list of str
            The texts corresponding to the answers
        train_start_indices, eval_start_indices: list of int
            The character positions of the start of the answers
        max_seq_length:int
            The maximum total input sequence length after tokenization.
        doc_stride: int
            When splitting up a long document into chunks, how much stride to take between chunks.
        max_query_length: int
            The maximum number of tokens for the question.
        freeze_base: Boolean
            Whether to freeze the weights of the base model, so training only changes the task head weights.
            If true, the requires_grad flag for parameters of the base model will be set to false before training.
        task_learn_rate: float
            Learning rate to be used for task specific parameters, (base parameters will use the normal, ie already
            defined in **training_args, learning rate). If None, all parameters will use the same normal learning rate.
        collator: Transformers.DataCollator
            custom collator to use
        train_dataset, eval_dataset: torch.Dataset
            instantiated custom dataset object
        compute_metrics: function
            The function that will be used to compute metrics at evaluation. Must return a dictionary string to metric
            values. Used by the trainer, see https://huggingface.co/transformers/training.html#trainer for more info.
        trainer: Transformers.Trainer
            custom instantiated trainer to use
        training_args:
            keyword arguments for training. For complete list, see
            https://huggingface.co/transformers/main_classes/trainer.html#transformers.TrainingArguments
        """
        if freeze_base:
            freeze_base_layers(self.model)
        if trainer is None:
            if self.model_device.type == "cpu":
                training_args["no_cuda"] = True
            if output_dir is None:
                raise RuntimeError("Must provide output directory argument to train() method if trainer argument is "
                                   "None")
            if train_dataset is None:
                if train_question_texts is None or train_context_texts is None or train_answer_texts is None or \
                        train_start_indices is None:
                    raise RuntimeError("Incomplete training data provided to train method")
                train_dataset = MangoesQuestionAnsweringDataset(self.tokenizer, train_question_texts,
                                                                train_context_texts, train_answer_texts,
                                                                train_start_indices, max_seq_length, doc_stride,
                                                                max_query_length)
            if eval_question_texts is not None and eval_context_texts is not None and eval_answer_texts is not None and \
                    eval_start_indices is not None and eval_dataset is None:
                eval_dataset = MangoesQuestionAnsweringDataset(self.tokenizer, eval_question_texts,
                                                               eval_context_texts, eval_answer_texts,
                                                               eval_start_indices, max_seq_length, doc_stride,
                                                               max_query_length)
            if eval_dataset is not None and "evaluation_strategy" not in training_args:
                training_args["evaluation_strategy"] = "epoch"
            train_args = transformers.TrainingArguments(output_dir=output_dir, **training_args)
            if task_learn_rate is not None:
                trainer = MultipleLearnRateFineTuneTrainer(task_learn_rate=task_learn_rate,
                                                           task_weight_decay=train_args.weight_decay,
                                                           model=self.model, args=train_args,
                                                           train_dataset=train_dataset,
                                                           data_collator=collator, eval_dataset=eval_dataset,
                                                           tokenizer=self.tokenizer, compute_metrics=compute_metrics)
            else:
                trainer = transformers.Trainer(self.model, args=train_args, train_dataset=train_dataset,
                                               data_collator=collator, eval_dataset=eval_dataset,
                                               tokenizer=self.tokenizer, compute_metrics=compute_metrics)
        self.trainer = trainer
        self.trainer.train()
        self.model.eval()


class TransformerForMultipleChoice(TransformerModel):
    """
    Pretrained model with a multiple choice classification head on top (a linear layer on top of the pooled output and a
    softmax) e.g. for RocStories/SWAG tasks.

    For a list of eligible model classes, see:
    https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForMultipleChoice.from_config.config

    For information on how multiple choice datasets should be formatted for fine-tuning, see this explanation:
    https://github.com/google-research/bert/issues/38

    And this link for explanation of Huggingface's multiple choice models:
    https://github.com/huggingface/transformers/issues/7701#issuecomment-707149546

    :var self.tokenizer: transformers.AutoTokenizerFast object,
        see https://huggingface.co/docs/transformers/model_doc/auto for more documentation
    :var self.model: transformers.AutoModelForMultipleChoice object,
        see https://huggingface.co/docs/transformers/model_doc/auto

    Parameters
    ----------
    pretrained_model: str, transformers.PretrainedModel subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated transformer model, either an transformers.AutoModelForMultipleChoice
              compatible class or a mangoes enhanced language model.
    pretrained_tokenizer: str, transformers.PreTrainedTokenizerBase subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated tokenizer, either an transformers.AutoTokenizer compatible class or a mangoes
              enhanced language model tokenizer.
    device: int, optional, defaults to None
        if -1, use cpu, if >= 0, use CUDA device number. If None, will use GPU if available
    **keyword_args include arguments passed to transformers.AutoConfig
    """

    def __init__(self, pretrained_model, pretrained_tokenizer, device=None, **keyword_args):
        keyword_args["ignore_mismatched_sizes"] = True
        TransformerModel.__init__(self, pretrained_model, pretrained_tokenizer,
                                  transformers.AutoModelForMultipleChoice, device, **keyword_args)
        if self.tokenizer.pad_token is None:  # to allow batching during training, need to be able to pad
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.config.pad_token_id = self.model.config.eos_token_id

    def generate_outputs(self, questions, choices, pre_tokenized=False, output_attentions=False,
                         output_hidden_states=False, word_embeddings=False, **tokenizer_inputs):
        """
        Tokenize context and choices and pass them through the model and MC head,
        optionally outputting hidden states or attention matrices.
        Works for a single question/set of choices or a batch. If a single question/set of choices is given, a batch of
        size 1 will be created.

        Follows these explanations for packing MC data and sending it through the model:
            https://github.com/google-research/bert/issues/38
            https://github.com/huggingface/transformers/issues/7701#issuecomment-7071495

        Parameters
        ----------
        questions: str or List[str] if pre_tokenized=False, else List[str] or List[List[str]]
            The question text. This can include the context together with a question, or (in the case of some datasets
            such as the SWAG dataset) just the context if there is no direct question. Can be a single question or list
            of questions.
        choices: List[str] or List[List[str]] if pre_tokenized=False, else List[List[str]] or List[List[List[str]]]
            The choices text. One instance of choices should be a list of strings (if not pre-tokenized) or a list of
            list of strings (if pre-tokenized). Can be a single choice instance or multiple.
            If batch is passed in (ie more than one question), assumes all questions have same number of choices.
        pre_tokenized: Boolean
            Whether or not the input text is pre-tokenized (ie, split on spaces)
        output_attentions: Boolean, optional, defaults to False
            Whether or not to return the attentions tensors of all attention layers.
        output_hidden_states: Boolean, optional, defaults to False
            Whether or not to return the hidden states of all layers.
        word_embeddings: Boolean
            Whether or not to filter special token embeddings and average subword embeddings (hidden states) into word
            embeddings. This functionality is not available for this task class. Use the feature extraction class
            instead.
        tokenizer_inputs: tokenizer_inputs include arguments passed to tokenizer, such as presaved entity annotations
            for enhanced models.

        Returns
        -------
        Dict containing (note that if single question/set of choices is passed as input, batch size will be 1):
        logits: Tensor of shape (batch_size, num_choices)
            Classification scores (before SoftMax). If batch
        offset_mappings: Tensor of shape (batch_size, num_choices, sequence_length, 2)
            Tensor containing (char_start, char_end) for each token, giving index into input strings of start and end
            character for each token. If input is pre-tokenized, start and end index maps into associated word. Note
            that special tokens are included with 0 for start and end indices, as these don't map into input text
            because they are added inside the function. Offset mappings for both questions and choices are merged to one
            row, but indices still align to them separately.
        hidden_states: Tuple (one for each layer) of torch.FloatTensor of size
            (batch_size, num_choices, sequence_length, hidden_size)
            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
            Only returned if output_hidden_states is True
        attentions: Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_choices, num_heads,
            sequence_length, sequence_length).
            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
            Only returned if output_attentions is True
        """
        # make batch of 1 if single question
        if isinstance(questions, str) or (isinstance(questions[0], str) and pre_tokenized):
            questions = [questions]
        if isinstance(choices[0], str) or (isinstance(choices[0][0], str) and pre_tokenized):
            choices = [choices]
        if len(questions) != len(choices):
            raise RuntimeError("Number of questions does not match number of sets of choices, "
                               "please checkxt classification inputs. Refer to the method documentation for input "
                               "format")
        batch_size = len(questions)
        num_choices = len(choices[0])
        for i in range(batch_size):
            questions[i] = [questions[i]] * num_choices
        # flatten into one batch of (batch_size * num_choices) sequences
        questions = [single_choice_question for question in questions for single_choice_question in question]
        choices = [single_choice for choice_list in choices for single_choice in choice_list]
        inputs = self.tokenizer(
            text=questions,
            text_pair=choices,
            padding=True,
            truncation=True,
            is_split_into_words=pre_tokenized,
            max_length=self.tokenizer.model_max_length,
            return_tensors="pt",
            return_offsets_mapping=True if isinstance(self.tokenizer, transformers.PreTrainedTokenizerFast) else False,
            return_token_type_ids=True,
            return_special_tokens_mask=True,
            return_overflowing_tokens=False,
            **tokenizer_inputs
        )
        if 'offset_mapping' in inputs:
            offset_mappings = inputs.pop('offset_mapping')
            offset_mappings = offset_mappings.view(batch_size, num_choices, -1, 2)
        else:
            offset_mappings = None
        inputs = {name: tensor for name, tensor in inputs.items() if name in self.tokenizer.model_input_names}
        sequence_length = inputs["input_ids"].size(-1)
        for k, v in inputs.items():
            new_shape = (batch_size, num_choices) + tuple(int(x) for x in list(v.shape[1:]))
            inputs[k] = v.view(new_shape)

        self.model.eval()
        if word_embeddings:
            warnings.warn("Word embedding consolidation not available for Multiple Choice model. Consider using the "
                          "mangoes.modeling.TransformerForFeatureExtraction class for feature "
                          "extractions")
        with torch.no_grad():
            if self.model_device.type == "cuda":
                inputs = {name: tensor.to(self.model_device) for name, tensor in inputs.items()}
            results = self.model.forward(**inputs, return_dict=True, output_attentions=output_attentions,
                                         output_hidden_states=output_hidden_states)
        if output_hidden_states:
            resized_hidden_states = []
            for i in range(len(results["hidden_states"])):
                resized_hidden_states.append(results["hidden_states"][i]
                                             .view(batch_size, num_choices, sequence_length, -1))
            results["hidden_states"] = tuple(resized_hidden_states)
        if output_attentions:
            resized_attentions = []
            for i in range(len(results["attentions"])):
                resized_attentions.append(results["attentions"][i]
                                          .view(batch_size, num_choices, -1, sequence_length, sequence_length))
            results["attentions"] = tuple(resized_attentions)
        results["offset_mappings"] = offset_mappings
        return results

    def predict(self, questions, choices, pre_tokenized=False):
        """
        Predicts the answer to the question(s) out of the possible choices.

        Parameters
        ----------
        questions: str or List[str] if pre_tokenized=False, else List[str] or List[List[str]]
            The question text. This can include the context together with a question, or (in the case of some datasets
            such as the SWAG dataset) just the context if there is no direct question. Can be a single question or list
            of questions.
        choices: List[str] or List[List[str]] if pre_tokenized=False, else List[List[str]] or List[List[List[str]]]
            The choices text. One instance of choices should be a list of strings (if not pre-tokenized) or a list of
            list of strings (if pre-tokenized). Can be a single choice instance or multiple.
            If batch is passed in (ie more than one question), assumes all questions have same number of choices.
        pre_tokenized: Boolean
            Whether or not the input text is pre-tokenized (ie, split on spaces)

        Returns
        -------
        List of answer prediction dicts, one for each question (returns list of length 1 if single question is passed as
        input. Answer prediction dicts include:
        score: float
            The probability associated to the answer.
        answer_index: int
            The index of the predicted choice.
        answer_text: str (if not pre_tokenized) or List[str] (if pre_tokenized)
            The text corresponding to the predicted answer.
        """
        outputs = self.generate_outputs(questions, choices, pre_tokenized)
        if isinstance(choices[0], str) or (pre_tokenized and isinstance(choices[0][0], str)):
            choices = [choices]
        outputs["logits"] = F.softmax(outputs["logits"], dim=-1)
        predictions = []
        for i in range(len(outputs["logits"])):
            answer_dict = {"answer_index": torch.argmax(outputs["logits"][i]).item()}
            answer_dict["score"] = outputs["logits"][i][answer_dict["answer_index"]].item()
            answer_dict["answer_text"] = choices[i][answer_dict["answer_index"]]
            predictions.append(answer_dict)
        return predictions

    def train(self, output_dir=None, train_question_texts=None, eval_question_texts=None, train_choices_texts=None,
              eval_choices_texts=None, train_labels=None, eval_labels=None, max_len=None, freeze_base=False,
              task_learn_rate=None, collator=None, train_dataset=None, eval_dataset=None, compute_metrics=None,
              trainer=None, **training_args):
        """
        Fine tune a pretrained model on a multiple choice dataset

        Parameters
        ----------
        output_dir: str
            Path to the output directory where the model predictions and checkpoints will be written. Used to
            instantiate Trainer if trainer argument is None.
        train_question_texts, eval_question_texts: list of str
            The texts corresponding to the questions/contexts.
        train_choices_texts, eval_choices_texts: list of str
            The texts corresponding to the answer choices
        train_labels, eval_labels: list of int
            The indices of the correct answers
        max_len:int
            The maximum total input sequence length after tokenization. Note that if a question answer pair sequence is
            longer than this length, it will be truncated.
        freeze_base: Boolean
            Whether to freeze the weights of the base model, so training only changes the task head weights.
            If true, the requires_grad flag for parameters of the base model will be set to false before training.
        task_learn_rate: float
            Learning rate to be used for task specific parameters, (base parameters will use the normal, ie already
            defined in **training_args, learning rate). If None, all parameters will use the same normal learning rate.
        collator: Transformers.DataCollator
            custom collator to use
        train_dataset, eval_dataset: torch.Dataset
            instantiated custom dataset object
        compute_metrics: function
            The function that will be used to compute metrics at evaluation. Must return a dictionary string to metric
            values. Used by the trainer, see https://huggingface.co/transformers/training.html#trainer for more info.
        trainer: Transformers.Trainer
            custom instantiated trainer to use
        training_args:
            keyword arguments for training. For complete list, see
            https://huggingface.co/transformers/main_classes/trainer.html#transformers.TrainingArguments
        """
        if freeze_base:
            freeze_base_layers(self.model)
        if trainer is None:
            if self.model_device.type == "cpu":
                training_args["no_cuda"] = True
            if output_dir is None:
                raise RuntimeError("Must provide output directory argument to train() method if trainer argument is "
                                   "None")
            if train_dataset is None:
                if train_question_texts is None or train_choices_texts is None or train_labels is None:
                    raise RuntimeError("Incomplete training data provided to train method")
                train_dataset = MangoesMultipleChoiceDataset(self.tokenizer, train_question_texts, train_choices_texts,
                                                             train_labels)
            if eval_question_texts is not None and eval_choices_texts is not None and eval_labels is not None and \
                    eval_dataset is None:
                eval_dataset = MangoesMultipleChoiceDataset(self.tokenizer, eval_question_texts, eval_choices_texts,
                                                            eval_labels)
            if eval_dataset is not None and "evaluation_strategy" not in training_args:
                training_args["evaluation_strategy"] = "epoch"
            train_args = transformers.TrainingArguments(output_dir=output_dir, **training_args)
            if collator is None:
                collator = DataCollatorForMultipleChoice(self.tokenizer)
            if task_learn_rate is not None:
                trainer = MultipleLearnRateFineTuneTrainer(task_learn_rate,
                                                           task_weight_decay=train_args.weight_decay,
                                                           model=self.model, args=train_args,
                                                           data_collator=collator, train_dataset=train_dataset,
                                                           eval_dataset=eval_dataset, tokenizer=self.tokenizer,
                                                           compute_metrics=compute_metrics)
            else:
                trainer = transformers.Trainer(self.model, args=train_args, train_dataset=train_dataset,
                                               data_collator=collator, eval_dataset=eval_dataset,
                                               tokenizer=self.tokenizer, compute_metrics=compute_metrics)
        self.trainer = trainer
        self.trainer.train()
        self.model.eval()


class TransformerForCoreferenceResolution(TransformerModel):
    """Class for fine tuning a transformer model for the coreference resolution task.

    The base model is an implementation of the independent variant of https://arxiv.org/pdf/1908.09091.pdf, which uses
    the fine tuning procedure described in https://arxiv.org/pdf/1804.05392.pdf

    :var self.tokenizer: transformers.AutoTokenizerFast object,
        see https://huggingface.co/docs/transformers/model_doc/auto for more documentation
    :var self.model: transformers.AutoModel object,
        see https://huggingface.co/docs/transformers/model_doc/auto

    Parameters
    ----------
    pretrained_model: str, transformers.PretrainedModel subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated transformer model, either an transformers.
              compatible class or a mangoes enhanced language model.
    pretrained_tokenizer: str, transformers.PreTrainedTokenizerBase subclass.
        Either:
            - A string with the `shortcut name` of a pretrained model to load from cache or download, e.g.,
              ``bert-base-uncased``.
            - A string with the `identifier name` of a pretrained model that was user-uploaded to our S3, e.g.,
              ``dbmdz/bert-base-german-cased``.
            - A path to a `directory` containing model weights saved using
              :func:`~save_pretrained`, e.g., ``./my_model_directory/``.
            - An already instantiated tokenizer, either an transformers.AutoTokenizer compatible class or a mangoes
              enhanced language model tokenizer.
    device: int, optional, defaults to None
        If -1, use cpu, if >= 0, use CUDA device number. If None, will use GPU if available.
    max_span_width: int, defaults to 30
        Maximum width (consecutive tokens) of candidate span.
    ffnn_hidden_size: int, defaults to 1000
        Size of hidden layers in dense mention scorer and slow antecedent scorer heads.
    top_span_ratio: float, defaults to 0.4
        Ratio of spans to consider after first sort on mention score.
    max_top_antecendents" int, defaults to 50
        Max number of antecedents to consider for each span after fast antecedent scorer.
    use_metadata: Boolean, defaults to False
        Whether to use metadata (speaker and genre information) in forward pass.
    metadata_feature_size: int, defaults to 20
        Size of metadata features (if using metadata)
    genres: List of string, defaults to ("bc", "bn", "mz", "nw", "pt", "tc", "wb")
        List of possible genres (if using metadata). Defaults to genres in Ontonotes dataset.
    max_training_segments: int, defaults to 5
        Maximum number of segments in one document (aka one batch).
    coref_depth: int, defaults to 2
        Depth of higher order (aka slow) antecedent scoring.
    coref_dropout: float, defaults to 0.3
        Dropout probability for head layers.
    **keyword_args
    """

    def __init__(self, pretrained_model, pretrained_tokenizer, device=None, max_span_width=30,
                 ffnn_hidden_size=1000, top_span_ratio=0.4, max_top_antecendents=50, use_metadata=False,
                 metadata_feature_size=20, genres=("bc", "bn", "mz", "nw", "pt", "tc", "wb"), max_training_segments=5,
                 coref_depth=1, coref_dropout=0.3, pretrained=False, **keyword_args):
        # we instantiate the model/tokenizer here instead of in the base class as we not directly using an AutoModel.
        if isinstance(pretrained_tokenizer, str):
            tokenizer = transformers.AutoTokenizer.from_pretrained(pretrained_tokenizer, use_fast=False)
        elif not isinstance(pretrained_tokenizer, transformers.PreTrainedTokenizerBase):
            raise ValueError(f"pretrained_tokenizer argument should be either str or "
                             f"transformers.PreTrainedTokenizerBase subclass, got {type(pretrained_tokenizer)}")
        else:
            tokenizer = pretrained_tokenizer
        keyword_args["vocab_size"] = len(tokenizer.get_vocab())
        if pretrained and os.path.exists(os.path.join(pretrained_model, "config.json")):
            pretrained_config_path = os.path.join(pretrained_model, "config.json")
            pretrained_config = \
                TransformerModelForCoreferenceResolutionBase.config_class.from_pretrained(pretrained_config_path)
        else:
            pretrained_config = None
        if not pretrained:
            model = TransformerModelForCoreferenceResolutionBase(pretrained_model,
                                                                 max_span_width=max_span_width,
                                                                 ffnn_hidden_size=ffnn_hidden_size,
                                                                 top_span_ratio=top_span_ratio,
                                                                 max_top_antecendents=max_top_antecendents,
                                                                 use_metadata=use_metadata,
                                                                 metadata_feature_size=metadata_feature_size,
                                                                 genres=genres,
                                                                 max_training_segments=max_training_segments,
                                                                 coref_depth=coref_depth,
                                                                 coref_dropout=coref_dropout)
        elif isinstance(tokenizer, ErnieTokenizer) or \
                (pretrained_config is not None and hasattr(pretrained_config, "adapter_size")):
            # special cases for some of the enhanced models
            pretrained_config_path = os.path.join(pretrained_model, "config.json")
            pretrained_config = \
                TransformerModelForCoreferenceResolutionBase.config_class.from_pretrained(pretrained_config_path)
            state_dict = load_state_dict(os.path.join(pretrained_model, "pytorch_model.bin"))
            if isinstance(tokenizer, ErnieTokenizer):
                pretrained_model_instantiated = \
                    ErnieModel(pretrained_config,
                               kg_embeddings=state_dict["features_model.kg_embeddings.weight"].numpy())
            elif hasattr(pretrained_config, "adapter_size"):
                pretrained_model_instantiated = KAdapterModel(pretrained_config)
            model = TransformerModelForCoreferenceResolutionBase(
                pretrained_model_instantiated,
                max_span_width=pretrained_config.task_specific_params["max_span_width"],
                ffnn_hidden_size=pretrained_config.task_specific_params["ffnn_hidden_size"],
                top_span_ratio=pretrained_config.task_specific_params["top_span_ratio"],
                max_top_antecendents=pretrained_config.task_specific_params["max_top_antecendents"],
                use_metadata=pretrained_config.task_specific_params["use_metadata"],
                metadata_feature_size=pretrained_config.task_specific_params["metadata_feature_size"],
                genres=pretrained_config.task_specific_params["genres"],
                max_training_segments=pretrained_config.task_specific_params["max_training_segments"],
                coref_depth=pretrained_config.task_specific_params["coref_depth"],
                coref_dropout=pretrained_config.task_specific_params["coref_dropout"])
            model.load_state_dict(state_dict)
            model.tie_weights()
        else:
            model = TransformerModelForCoreferenceResolutionBase.from_pretrained(pretrained_model, keyword_args)
        TransformerModel.__init__(self, model, tokenizer, device=device)
        # TODO: coref datasets rely on pre-split inputs, the following line allows this to work for all tokenizers
        # should maybe refactor coref dataset class to not need this...
        if hasattr(self.tokenizer, "add_prefix_space"):
            self.tokenizer.add_prefix_space = True

    def predict(self, text, pre_tokenized=False, speaker_ids=None, genre=None, max_segment_len=256, max_segments=5):
        """
        Predict the co-reference clusters in text. Takes one document at a time. Internally calls generate_outputs and
        then processes the outputs.

        Parameters
        ----------
        text: str or List[str] if pre_tokenized=False, else List[str] or List[List[str]]
            The text to predict co-references for. If pre_tokenized, the text can be one sentence (list of words) or
            list of sentences (list of list of words). If not pre_tokenized, text can be one sentence (str) or list of
            sentences (list of strings).
        pre_tokenized: Boolean
            Whether or not the input text is pretokenized (ie, split on spaces). This method will still pass it through
            the tokenizer, in order to get subtokens, special characters, and attention masks.
        speaker_ids: int or List[int] if pre_tokenized=False, else List[int] or List[List[int]]
            Speaker ids for input text. If pre_tokenized, speaker_ids should be for each word in each sentence of input
            text (ie, list of int if one sentence, or list of list of int if multiple). If not pre_tokenized, speaker
            ids should be on a sentence basis, ie one int if one input sentence, or list of ints if multiple.
            Optional, needed only if the model has been trained/instantiated to accept metadata.
        genre: Int or String
            Genre of text. If string, will attempt to use the genre id mapping constructed by the model parameter to
            this object. Optional, needed only if the model has been trained/instantiated to accept metadata.
        max_segment_len: int, defaults to 256
            maximum number of sub-tokens for one segment
        max_segments: int, defaults to 5
            Maximum number of segments to return per document

        Returns
        -------
        List of dicts.
        For each found co-reference cluster, a dict with the following keys:
            cluster_tokens: List[List[str]]]
                The text spans associated with the cluster. Spans are represented by the list of tokens.
            cluster_ids: List[List[int]]
                The id spans associated with the cluster. Spans are represented by the list of token ids.
        """
        outputs = self.generate_outputs(text, pre_tokenized, speaker_ids, genre, max_segment_len, max_segments)
        top_indices = torch.argmax(outputs["top_antecedent_scores"], dim=-1, keepdim=False)

        mention_indices = []
        antecedent_indices = []
        for i in range(len(outputs["top_span_ends"])):
            if top_indices[i] > 0:
                mention_indices.append(i)
                antecedent_indices.append(outputs["top_antecedents"][i][top_indices[i] - 1].item())

        cluster_sets = []
        for i in range(len(antecedent_indices)):
            new_cluster = True
            for j in range(len(cluster_sets)):
                if mention_indices[i] in cluster_sets[j] or antecedent_indices[i] in cluster_sets[j]:
                    cluster_sets[j].add(mention_indices[i])
                    cluster_sets[j].add(antecedent_indices[i])
                    new_cluster = False
                    break
            if new_cluster:
                cluster_sets.append({mention_indices[i], antecedent_indices[i]})

        cluster_dicts = []
        for i in range(len(cluster_sets)):
            cluster_mentions = sorted(list(cluster_sets[i]))
            current_ids = []
            current_tokens = []
            for mention_index in cluster_mentions:
                current_ids.append(outputs["flattened_ids"]
                                   [outputs["top_span_starts"][mention_index]:
                                    outputs["top_span_ends"][mention_index] + 1])
                current_tokens.append(outputs["flattened_text"]
                                      [outputs["top_span_starts"][mention_index]:
                                       outputs["top_span_ends"][mention_index] + 1])
            cluster_dicts.append({"cluster_ids": current_ids, "cluster_tokens": current_tokens})
        return cluster_dicts

    def generate_outputs(self, text, pre_tokenized=False, speaker_ids=None, genre=None, output_attentions=False,
                         output_hidden_states=False, word_embeddings=False, max_segment_len=256, max_segments=5,
                         **tokenizer_inputs):
        """
        Pass one batch (document) worth of text through the co-reference model, outputting mention scores and token
        indices for possible spans, the indices and scores of the top antecedents for the top mention scored spans, and
        optionally the hidden states or attention matrices from the base model.

        Note that this functions does not return "offset_mappings", and instead returns the flattened ids and text.

        Parameters
        ----------
        text: str or List[str] if pre_tokenized=False, else List[str] or List[List[str]]
            The text to predict co-references for. If pre_tokenized, the text can be one sentence (list of words) or
            list of sentences (list of list of words). If not pre_tokenized, text can be one sentence (str) or list of
            sentences (list of strings).
        pre_tokenized: Boolean
            Whether or not the input text is pretokenized (ie, split on spaces). This method will still pass it through
            the tokenizer, in order to get subtokens, special characters, and attention masks.
        speaker_ids: int or List[int] if pre_tokenized=False, else List[int] or List[List[int]]
            Speaker ids for input text. If pre_tokenized, speaker_ids should be for each word in each sentence of input
            text (ie, list of int if one sentence, or list of list of int if multiple). If not pre_tokenized, speaker
            ids should be on a sentence basis, ie one int if one input sentence, or list of ints if multiple.
            Optional, needed only if the model has been trained/instantiated to accept metadata.
        genre: Int or String
            Genre of text. If string, will attempt to use the genre id mapping constructed by the model parameter to
            this object. Optional, needed only if the model has been trained/instantiated to accept metadata.
        output_attentions: Boolean, optional, defaults to False
            Whether or not to return the attentions tensors of all attention layers.
        output_hidden_states: Boolean, optional, defaults to False
            Whether or not to return the hidden states of all layers.
        word_embeddings: Boolean
            Whether or not to filter special token embeddings and average subword embeddings (hidden states) into word
            embeddings. Note: this functionality is not available for this class because of consolidation of input in
            the forward pass of the model. Consider using
            mangoes.modeling.TransformerForFeatureExtraction class for word-level feature extractions.
        max_segment_len: int, defaults to 256
            maximum number of sub-tokens for one segment
        max_segments: int, defaults to 5
            Maximum number of segments to return per document
        tokenizer_inputs: tokenizer_inputs include arguments passed to tokenizer, such as presaved entity annotations
            for enhanced models.

        Returns
        -------
        Dict containing:
        candidate_starts: tensor of size (num_spans)
            start token indices in flattened document of candidate spans
        candidate_ends: tensor of size (num_spans)
            end token indices in flattened document of candidate spans
        candidate_mention_scores: tensor of size (num_spans)
            mention scores for each candidate span
        top_span_starts: tensor of size (num_top_spans)
            start token indices in flattened document of candidate spans with top mention scores
        top_span_ends: tensor of size (num_top_spans)
            end token indices in flattened document of candidate spans with top mention scores
        top_antecedents: tensor of shape (num_top_spans, antecedent_candidates)
            indices in top span candidates of top antecedents for each mention
        top_antecedent_scores: tensor of shape (num_top_spans, 1 + antecedent_candidates)
            final antecedent scores of top antecedents for each mention. The dummy score (for not a co-reference) is
            inserted at the start of each row. Thus, the score for top_antecedents[0][0] is top_antecedent_scores[0][1].
            The span for first candidate is top_span_starts[0] to top_span_ends[0]. The span for the first top
            antecedent for the first candidate is top_span_starts[top_antecedents[0][0]] to
            top_span_ends[top_antecedents[0][0]].
        flattened_ids: tensor of shape (num_tokens)
            flattened ids of input sentences. The start and end candidate and span indices map into this tensor.
        flattened_text: tensor of shape (num_tokens)
            flattened tokens of input sentences. The start and end candidate and span indices map into this tensor.
        hidden_states: Tuple (one for each layer) of torch.FloatTensor (batch_size, sequence_length, hidden_size).
            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
            Only returned if output_hidden_states is True
        attentions: Tuple of torch.FloatTensor (one for each layer) of shape (batch_size, num_heads, sequence_length,
            sequence_length).
            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
            Only returned if output_attentions is True
        """
        if self.model.use_metadata:
            if not (speaker_ids is not None and genre is not None):
                raise RuntimeError("Co-reference model has been trained/initiated to use metadata, please provide "
                                   "speaker_ids argument and genre arguments.")
            if isinstance(genre, str):
                try:
                    genre = self.model.genres[genre]
                except KeyError:
                    raise RuntimeError("The genre argument passed to generate_outputs is not in the model's genre id "
                                       "mapping dictionary.")
            elif not isinstance(genre, int):
                raise RuntimeError("The genre argument must be a string or int.")
            if isinstance(text, list):
                if not len(speaker_ids) == len(text):
                    raise RuntimeError("Lengths of speaker ids and text arguments are different. See docstring of "
                                       "generate_outputs for appropriate input format.")
        # if single sentence, wrap in list
        if isinstance(text, str) or (pre_tokenized and isinstance(text[0], str)):
            text = [text]
            if self.model.use_metadata:
                speaker_ids = [speaker_ids]

        if not pre_tokenized:
            text = [sentence.split() for sentence in text]
            if self.model.use_metadata:
                speaker_ids = [[speaker_ids[i]] * len(text[i]) for i in range(len(text))]

        if not self.model.use_metadata:
            ids, attention_mask, sentence_map = make_coref_example(self.tokenizer, text, None, speaker_ids,
                                                                   self.model.use_metadata, max_segment_len)
        else:
            ids, attention_mask, sentence_map, speaker_ids = make_coref_example(self.tokenizer, text, None, speaker_ids,
                                                                                self.model.use_metadata,
                                                                                max_segment_len)
            genre = torch.as_tensor(genre)
        if len(ids) > max_segments:
            warnings.warn('Input text to generate_outputs exceeds maximum segments; truncating.', RuntimeWarning)
            ids = ids[:max_segments]
            attention_mask = attention_mask[:max_segments]
            num_tokens = attention_mask.sum()
            sentence_map = sentence_map[:num_tokens]
            if self.model.use_metadata:
                speaker_ids = speaker_ids[:max_segments]
        inputs = {
            "input_ids": ids,
            "attention_mask": attention_mask,
            "sentence_map": sentence_map,
        }
        if not all(input_name in inputs for input_name in self.tokenizer.model_input_names):
            input_text = self.tokenizer.batch_decode(inputs["input_ids"], clean_up_tokenization_spaces=True)
            extra_inputs = self.tokenizer(
                text=input_text,
                text_pair=None,
                padding="max_length",
                truncation=True,
                is_split_into_words=False,
                max_length=inputs["input_ids"].shape[-1],
                return_tensors="pt",
                return_token_type_ids=True,
                return_special_tokens_mask=True,
                return_offsets_mapping=False,
                return_overflowing_tokens=False
            )
            extra_inputs = {k: extra_inputs[k] for k in self.tokenizer.model_input_names if k not in inputs}
            inputs.update(extra_inputs)
        if self.model.use_metadata:
            inputs.update({"speaker_ids": speaker_ids, "genre": genre})
        self.model.eval()
        with torch.no_grad():
            if self.model_device.type == "cuda":
                inputs = {name: tensor.to(self.model_device) for name, tensor in inputs.items()}
            results = self.model.forward(**inputs, return_dict=True,
                                         output_attentions=output_attentions,
                                         output_hidden_states=output_hidden_states)
        if word_embeddings:
            warnings.warn("Word embedding consolidation not available for co-reference model. Consider using the"
                          "mangoes.modeling.TransformerForFeatureExtraction class for feature "
                          "extractions.")
        results = dict(results)
        results["flattened_text"] = self.tokenizer.convert_ids_to_tokens(results["flattened_ids"])
        return results

    def train(self, output_dir=None, max_segment_len=256, max_segments=5, freeze_base=False, task_learn_rate=None,
              task_weight_decay=None, train_documents=None, train_cluster_ids=None, train_speaker_ids=None,
              train_genres=None, eval_documents=None, eval_cluster_ids=None, eval_speaker_ids=None, eval_genres=None,
              train_dataset=None, eval_dataset=None, compute_metrics=None, trainer=None, **training_args):
        """
        Fine tune a pretrained model on a co-reference resolution dataset.
        Users can input the raw coreference data and a torch dataset will be created, or they can input already
        instantiated dataset(s), or an already instantiated trainer.

        Note that this implementation is based on the "independent" variant of the method introduced in
        https://arxiv.org/pdf/1908.09091.pdf, thus the batch size will be 1 (1 document per batch, with multiple
        segments per document), and a specific collator function will be used.

        Parameters
        ----------
        output_dir: str
            Path to the output directory where the model predictions and checkpoints will be written. Used to
            instantiate Trainer if trainer argument is None.
            Optional: needed if trainer is not provided
        max_segment_len: int, defaults to 256
            maximum number of sub-tokens for one segment
        max_segments: int, defaults to 5
            Maximum number of segments to return per document
        freeze_base: Boolean
            Whether to freeze the weights of the base model, so training only changes the task head weights.
            If true, the requires_grad flag for parameters of the base model will be set to false before training.
        task_learn_rate: float
            Learning rate to be used for task specific parameters, (base parameters will use the normal, ie already
            defined in **training_args, learning rate). If None, all parameters will use the same normal learning rate.
        task_weight_decay: float
            Weight decay parameter to be used for task specific parameters. (base parameters will use the normal, ie
            already defined in **training_args, weight decay). If None, all parameters will use the same normal weight
            decay.
        train_documents: List of Lists of Lists of strings
            Optional: needed if train_dataset or trainer is not provided
            Text for each document. As cluster ids are labeled by word, a document is a list of sentences. One
            sentence is a list of words (ie already split on whitespace/punctuation)
        train_cluster_ids: List of Lists of Lists of (ints or Tuple(int, int))
            Optional: needed if train_dataset or trainer is not provided
            Cluster ids for each word in documents argument. Assumes words that aren't mentions have either None or -1
            as id. In the case where a word belongs to two different spans (with different cluster ids), the cluster id
            for word should be a tuple of ints corresponding to the different cluster ids.
        train_speaker_ids: List of Lists of Lists of ints
            Optional: needed if train_dataset or trainer is not provided and model is using metadata
            Speaker id for each word in documents. Assumes positive ids (special tokens (such as [CLS] and [SEP] that
            are added at beginning and end of segments) will be assigned speaker ids of -1)
        train_genres: List of ints
            Optional: needed if train_dataset or trainer is not provided and model is using metadata
            Genre id for each document
        eval_documents: List of Lists of Lists of strings
            Optional: needed if train_dataset or trainer is not provided
            Text for each document. As cluster ids are labeled by word, a document is a list of sentences. One
            sentence is a list of words (ie already split on whitespace/punctuation)
        eval_cluster_ids: List of Lists of Lists of (ints or Tuple(int, int))
            Optional: needed if train_dataset or trainer is not provided
            Cluster ids for each word in documents argument. Assumes words that aren't mentions have either None or -1
            as id. In the case where a word belongs to two different spans (with different cluster ids), the cluster id
            for word should be a tuple of ints corresponding to the different cluster ids.
        eval_speaker_ids: List of Lists of Lists of ints
            Optional: needed if train_dataset or trainer is not provided and model is using metadata
            Speaker id for each word in documents. Assumes positive ids (special tokens (such as [CLS] and [SEP] that
            are added at beginning and end of segments) will be assigned speaker ids of -1)
        eval_genres: List of ints
            Optional: needed if train_dataset or trainer is not provided and model is using metadata
            Genre id for each document
        train_dataset, eval_dataset: torch.Dataset
            instantiated custom dataset object. Note that the model implementation and default trainer
            (mangoes.modeling.training_utils.CoreferenceFineTuneTrainer) are set up to work with
            mangoes.modeling.training_utils.MangoesCoreferenceDataset datasets, so take care when sending custom
            dataset arguments.
        compute_metrics: function
            The function that will be used to compute metrics at evaluation. Must return a dictionary string to metric
            values. Used by the trainer, see https://huggingface.co/transformers/training.html#trainer for more info.
        trainer: Transformers.Trainer
            custom instantiated trainer to use
        training_args:
            keyword arguments for training. For complete list, see
            https://huggingface.co/transformers/main_classes/trainer.html#transformers.TrainingArguments
        """
        if freeze_base:
            freeze_base_layers(self.model)
        if trainer is None:
            if self.model_device.type == "cpu":
                training_args["no_cuda"] = True
            if train_dataset is None:
                if train_documents is None or train_cluster_ids is None or \
                        (train_speaker_ids is None and self.model.config.task_specific_params["use_metadata"]) or \
                        (train_genres is None and self.model.config.task_specific_params["use_metadata"]):
                    raise RuntimeError("Incomplete training data provided to train method")
                train_dataset = MangoesCoreferenceDataset(self.tokenizer,
                                                          self.model.config.task_specific_params["use_metadata"],
                                                          max_segment_len, max_segments, train_documents,
                                                          train_cluster_ids, train_speaker_ids, train_genres,
                                                          self.model.genres)
            if eval_documents is not None and eval_cluster_ids is not None and \
                    (self.model.config.task_specific_params["use_metadata"] or (eval_speaker_ids is not None and
                                                                                eval_genres is not None)) \
                    and eval_dataset is None:
                eval_dataset = MangoesCoreferenceDataset(self.tokenizer,
                                                         self.model.config.task_specific_params["use_metadata"],
                                                         max_segment_len, max_segments, eval_documents,
                                                         eval_cluster_ids, eval_speaker_ids, eval_genres,
                                                         self.model.genres)
            if eval_dataset is not None and "evaluation_strategy" not in training_args:
                training_args["evaluation_strategy"] = "epoch"
            train_args = transformers.TrainingArguments(output_dir=output_dir, per_device_eval_batch_size=1,
                                                        per_device_train_batch_size=1,
                                                        label_names=["gold_starts", "gold_ends", "cluster_ids"],
                                                        **training_args)
            if task_learn_rate is None:
                task_learn_rate = train_args.learning_rate
            if task_weight_decay is None:
                task_weight_decay = train_args.weight_decay
            trainer = CoreferenceFineTuneTrainer(task_learn_rate, task_weight_decay, self.model.base_model_prefix,
                                                 self.model, args=train_args, train_dataset=train_dataset,
                                                 eval_dataset=eval_dataset, tokenizer=self.tokenizer,
                                                 compute_metrics=compute_metrics)
        self.trainer = trainer
        self.trainer.train()
        self.model.eval()
