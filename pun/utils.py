"""
pun.utils
=========

Utility used on pun.
"""

import sys
from importlib import import_module
from contextlib import contextmanager


@contextmanager
def import_file(pun_path):
    path_bak = sys.path[:]
    sys.path = [str(pun_path.parent.resolve())] + path_bak

    try:
        pf = import_module(pun_path.name.split('.')[0])
        yield pf
    except ImportError:
        yield None
    finally:
        sys.path = path_bak[:]
