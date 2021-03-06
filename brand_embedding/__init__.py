import os
import sys
import logging

__author__ = "roopal_garg"
__version__ = (1, 0, 0)


logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)

logger = logging.getLogger(__name__)

_brand_list_fpath = os.path.join(os.path.dirname(__file__), 'data/brand_list')
DEFAULT_SET_BRANDS = set()
with open(_brand_list_fpath) as fp:
    for line in fp.readlines():
        line = line.strip()
        if not line:
            continue
        DEFAULT_SET_BRANDS.add(line)

DEFAULT_BRAND_EMB_SAVE_FPATH = os.path.join(os.path.dirname(__file__), 'data/brand_emb.json')

_home_dir = os.path.expanduser('~')

ENV_EMBEDDING_GLOVE_6B_FPATH = os.path.join(os.path.dirname(__file__), 'data/glove_embeddings/glove.6B.{dim}d.txt')
