import os
import tarfile
from ...utils.file_utils import download_and_cache, MANGOES_CACHE_PATH
from transformers import RobertaModel, RobertaForSequenceClassification, RobertaForMultipleChoice, \
    RobertaForTokenClassification, RobertaForQuestionAnswering


KEPLER_DIR = os.path.join(MANGOES_CACHE_PATH, "kepler/")
KEPLER_ARCHIVE_PATH = os.path.join(MANGOES_CACHE_PATH, "kepler/kepler_transformers.tar.xz")
KEPLER_PRETRAINED_DIR = os.path.join(KEPLER_DIR, "kepler_transformers")
KEPLER_URL = "http://chercheurs.lille.inria.fr/magnet/kepler_transformers.tar.xz"
KEPLER_PRETRAINED_TOKENIZER_NAME = "roberta-base"


def download_extract_kepler_weights():
    """
    Downloads the the kepler pretrained weights and tokenizer.
    """
    if not os.path.exists(KEPLER_ARCHIVE_PATH):
        print("Downloading kepler pretrained model...")
        download_and_cache(KEPLER_URL, "kepler_transformers.tar.xz", cache_dir=KEPLER_DIR)
    if not os.path.exists(KEPLER_PRETRAINED_DIR):
        with tarfile.open(KEPLER_ARCHIVE_PATH) as f:
            f.extractall(KEPLER_DIR)


class KeplerModel(RobertaModel):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_kepler_weights()
            return super().from_pretrained(KEPLER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class KeplerForSequenceClassification(RobertaForSequenceClassification):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, labels=None, label2id=None, **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        if pretrained_model_name_or_path is None:
            download_extract_kepler_weights()
            return super().from_pretrained(KEPLER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class KeplerForTokenClassification(RobertaForTokenClassification):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, labels=None, label2id=None, **kwargs):
        if label2id is None and labels is None:
            raise RuntimeError("Must provide either labels or label to id mapping")
        if label2id is None:
            label2id = {tag: id for id, tag in enumerate(set(labels))}
        kwargs["id2label"] = {id: tag for tag, id in label2id.items()}
        if pretrained_model_name_or_path is None:
            download_extract_kepler_weights()
            return super().from_pretrained(KEPLER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class KeplerForQuestionAnswering(RobertaForQuestionAnswering):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_kepler_weights()
            return super().from_pretrained(KEPLER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)


class KeplerForMultipleChoice(RobertaForMultipleChoice):
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        if pretrained_model_name_or_path is None:
            download_extract_kepler_weights()
            return super().from_pretrained(KEPLER_PRETRAINED_DIR, *model_args, **kwargs)
        else:
            return super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)

