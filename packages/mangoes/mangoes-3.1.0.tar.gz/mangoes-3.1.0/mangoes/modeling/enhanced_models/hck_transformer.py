import os
import tarfile
from ...utils.file_utils import download_and_cache, MANGOES_CACHE_PATH
from transformers import BertModel, BertForSequenceClassification, BertForMultipleChoice, \
    BertForTokenClassification, BertForQuestionAnswering, BertTokenizerFast, BertTokenizer

HCK_DIR = os.path.join(MANGOES_CACHE_PATH, "hck_transformer/")
HCK_ARCHIVE_PATH = os.path.join(MANGOES_CACHE_PATH, "hck_transformer/hck_transformer.tar.xz")
HCK_PRETRAINED_DIR = os.path.join(HCK_DIR, "hck_transformer")
HCK_URL = "http://chercheurs.lille.inria.fr/magnet/hck_transformer.tar.xz"


def download_extract_hck_weights():
    """
    Downloads the the hck pretrained weights and tokenizer.
    """
    if not os.path.exists(HCK_ARCHIVE_PATH):
        print("Downloading human conceptual knowledge pretrained model...")
        download_and_cache(HCK_URL, "hck_transformer.tar.xz", cache_dir=HCK_DIR)
    if not os.path.exists(HCK_PRETRAINED_DIR):
        with tarfile.open(HCK_ARCHIVE_PATH) as f:
            f.extractall(HCK_DIR)


class HCKTokenizerFast(BertTokenizerFast):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_hck_weights()
            return super().from_pretrained(HCK_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class HCKTokenizer(BertTokenizer):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_hck_weights()
            return super().from_pretrained(HCK_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class HCKModel(BertModel):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_hck_weights()
            return super().from_pretrained(HCK_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class HCKForSequenceClassification(BertForSequenceClassification):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, labels=None, label2id=None, **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        if pretrained_model_name_or_path is None:
            download_extract_hck_weights()
            return super().from_pretrained(HCK_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class HCKForTokenClassification(BertForTokenClassification):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, labels=None, label2id=None, **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        if pretrained_model_name_or_path is None:
            download_extract_hck_weights()
            return super().from_pretrained(HCK_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class HCKForQuestionAnswering(BertForQuestionAnswering):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_hck_weights()
            return super().from_pretrained(HCK_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class HCKForMultipleChoice(BertForMultipleChoice):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_hck_weights()
            return super().from_pretrained(HCK_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)
