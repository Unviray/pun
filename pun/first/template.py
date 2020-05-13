"""
Pun
===

Pun mini task to build, deploy or anything you like in your project.
"""

# This is your default subsets of task when task target is not found in
# current punfile.

# You can edit this.

import pun


@pun.task()
def help(punned):
    """
    Show list of task and their description.
    """

    # make default to None for printing helper
    default = punned.default
    punned.default = None

    pun.run(punned.run)

    punned.default = default


@pun.task()
def init():
    """
    Create an empty punfile.
    """

    pun.run('touch punfile.py')
