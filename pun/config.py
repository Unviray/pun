"""
pun.config
==========

Load Configuration.
"""

from pathlib import Path

from .utils import import_file


class Config(object):
    HOME = Path().home() / '.pun'
    DEFAULT_PF = HOME / 'default_punfile.py'
    DEFAULT_CONFIG = HOME / 'config.py'

    PARENT_LEN = 2

    def __init__(self):
        with import_file(self.DEFAULT_CONFIG) as c:
            self.config_file = c

        self.setup()

    def setup(self, config_file=None):
        self.PARENT_LEN = getattr(config_file or self.config_file,
                                  'PARENT_LEN',
                                  self.PARENT_LEN)
