"""
pun.config
==========

Load Configuration.
"""

from pathlib import Path


class Config(object):
    PARENT_LEN = 2
    HOME = Path().home() / '.pun'
    DEFAULT_PF = HOME / 'default_punfile.py'
