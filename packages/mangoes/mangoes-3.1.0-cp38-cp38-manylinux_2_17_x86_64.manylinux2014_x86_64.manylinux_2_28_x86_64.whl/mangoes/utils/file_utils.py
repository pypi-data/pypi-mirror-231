import os
from pathlib import Path
import urllib.request
import shutil
import zipfile
import tempfile


MANGOES_CACHE_PATH = os.path.expanduser(
    os.getenv("MANGOES_CACHE", os.path.join("~/.cache", "mangoes"))
)


def download_and_cache(url, filename, cache_dir=None, force_download=False):
    """
    Download a file from a url and cache it.

    Parameters
    ----------
    url: str
        url to download from
    filename: str
        filename to save downloaded file
    cache_dir: str, optional
        if you want to specify a cache directory different than the default ("~/.cache/mangoes")
    force_download: bool
        If you want to download the file even if it is already in the cache.

    Returns
    -------
    output_path: str
        Local path (string) of file.
    """
    if cache_dir is None:
        cache_dir = MANGOES_CACHE_PATH
    if isinstance(cache_dir, Path):
        cache_dir = str(cache_dir)
    os.makedirs(cache_dir, exist_ok=True)
    cache_path = os.path.join(cache_dir, filename)
    if os.path.exists(cache_path) and not force_download:
        return cache_path
    temp_file_name = http_get(url, cache_dir)
    os.replace(temp_file_name, cache_path)
    return cache_path


def http_get(url, cache_dir):
    temp_file = tempfile.NamedTemporaryFile(mode="wb", dir=cache_dir, delete=False)
    try:
        with urllib.request.urlopen(url) as response, open(temp_file.name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            return temp_file.name
    except (Exception, KeyboardInterrupt):
        os.remove(temp_file.name)
        raise


def extract_zip(zip_path, extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

