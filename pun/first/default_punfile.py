"""
Pun
===

Pun mini task to build, deploy or anything you like in your project.
"""

# This is your default subsets of task when task target is not found in
# current punfile.

# You can edit this.

import pun


init_template = """
import pun


DEFAULT = 'default'


@pun.task()
def default():
    \"\"\"
    Run default action.
    \"\"\"

    text = "This is a sample punfile (you can edit)"

    pun.run('echo', text)
"""


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
    with open('punfile.py', 'w') as fp:
        fp.write(init_template)
