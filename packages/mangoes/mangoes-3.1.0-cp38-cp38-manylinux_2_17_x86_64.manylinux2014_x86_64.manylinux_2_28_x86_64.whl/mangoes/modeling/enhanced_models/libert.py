import os
import tarfile
from ...utils.file_utils import download_and_cache, MANGOES_CACHE_PATH
from transformers import BertModel, BertForSequenceClassification, BertForMultipleChoice, \
    BertForTokenClassification, BertForQuestionAnswering, BertTokenizerFast, BertTokenizer

LIBERT_DIR = os.path.join(MANGOES_CACHE_PATH, "libert/")
LIBERT_ARCHIVE_PATH = os.path.join(MANGOES_CACHE_PATH, "libert/libert.tar.xz")
LIBERT_PRETRAINED_DIR = os.path.join(LIBERT_DIR, "libert")
LIBERT_URL = "http://chercheurs.lille.inria.fr/magnet/libert.tar.xz"


def download_extract_libert_weights():
    """
    Downloads the the libert pretrained weights and tokenizer.
    """
    if not os.path.exists(LIBERT_ARCHIVE_PATH):
        print("Downloading libert pretrained model...")
        download_and_cache(LIBERT_URL, "libert.tar.xz", cache_dir=LIBERT_DIR)
    if not os.path.exists(LIBERT_PRETRAINED_DIR):
        with tarfile.open(LIBERT_ARCHIVE_PATH) as f:
            f.extractall(LIBERT_DIR)


class LibertTokenizerFast(BertTokenizerFast):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_libert_weights()
            return super().from_pretrained(LIBERT_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class LibertTokenizer(BertTokenizer):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_libert_weights()
            return super().from_pretrained(LIBERT_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class LibertModel(BertModel):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_libert_weights()
            return super().from_pretrained(LIBERT_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class LibertForSequenceClassification(BertForSequenceClassification):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, labels=None, label2id=None, **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        if pretrained_model_name_or_path is None:
            download_extract_libert_weights()
            return super().from_pretrained(LIBERT_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class LibertForTokenClassification(BertForTokenClassification):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, labels=None, label2id=None, **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        if pretrained_model_name_or_path is None:
            download_extract_libert_weights()
            return super().from_pretrained(LIBERT_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class LibertForQuestionAnswering(BertForQuestionAnswering):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_libert_weights()
            return super().from_pretrained(LIBERT_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class LibertForMultipleChoice(BertForMultipleChoice):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_libert_weights()
            return super().from_pretrained(LIBERT_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)
