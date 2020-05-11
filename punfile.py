import pun

DEFAULT = 'install'


@pun.task()
def install():
    """
    Install current package.
    """

    pun.run('touch', 'foo')


@pun.task()
def install_dev():
    """
    Install current package for development.
    """

    pun.run('touch bar')


@pun.task(install_dev)
def docs():
    """
    Build documentations.
    """

    with pun.cd('./pun'):
        pun.run('touch sss')


# pun.tasky('req', 'pip install -r requirements.txt')
