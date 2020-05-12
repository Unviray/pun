"""
Pun
===

Pun mini task to build, deploy or anything you like in your project.
"""

import pun

import os
import webbrowser

try:
    from urllib import pathname2url
except ImportError:
    from urllib.request import pathname2url


def browser(path):
    webbrowser.open("file://" + pathname2url(os.path.abspath(path)))


DEFAULT = 'default'


@pun.task('clean_build', 'clean_pyc', 'clean_test')
def clean():
    """
    Remove all build, test, coverage and Python artifacts.
    """


@pun.task()
def clean_build():
    """
    Remove build artifacts.
    """

    pun.run("rm -fr build/")
    pun.run("rm -fr dist/")
    pun.run("rm -fr .eggs/")
    pun.run("find . -name '*.egg-info' -exec rm -fr {} +")
    pun.run("find . -name '*.egg' -exec rm -f {} +")


@pun.task()
def clean_pyc():
    """
    Remove Python file artifacts.
    """

    pun.run("find . -name '*.pyc' -exec rm -f {} +")
    pun.run("find . -name '*.pyo' -exec rm -f {} +")
    pun.run("find . -name '*~' -exec rm -f {} +")
    pun.run("find . -name '__pycache__' -exec rm -fr {} +")


@pun.task()
def clean_test():
    """
    Remove test and coverage artifacts.
    """

    pun.run("rm -fr .tox/")
    pun.run("rm -f .coverage")
    pun.run("rm -fr htmlcov/")
    pun.run("rm -fr .pytest_cache")


@pun.task()
def lint():
    """
    Check style with flake8.
    """

    pun.run('flake8 pun tests')


@pun.task()
def test():
    """
    Run tests quickly with the default Python.
    """

    pun.run('pytest')


@pun.task()
def test_all():
    """
    Run tests on every Python version with tox.
    """

    pun.run('tox')


@pun.task()
def coverage():
    """
    Check code coverage quickly with the default Python.
    """

    pun.run("coverage run --source pun -m pytest")
    pun.run("coverage report -m")
    pun.run("coverage html")
    pun.run(browser, "htmlcov/index.html")


@pun.task('dist')
def release():
    """
    Package and upload a release.
    """

    pun.run('twine upload dist/*')


@pun.task(clean)
def dist():
    """
    Builds source and wheel package.
    """

    pun.run("python setup.py sdist")
    pun.run("python setup.py bdist_wheel")
    pun.run("ls -l dist")


@pun.task(clean)
def install():
    """
    Install the package to the active Python's site-packages.
    """

    pun.run('pip install .')


@pun.task()
def install_dev():
    """
    Install the package for development.
    """

    pun.run('pip install -e .')


# For testing
@pun.task()
def touch():
    """
    Create file in current directory.
    """

    pun.run('touch file')


@pun.task()
def remove():
    """
    Remove file in current directory.
    """

    pun.run('rm file')


@pun.task()
def touch_cd():
    """
    Create file in current directory.
    """

    with pun.cd('./tests'):
        pun.run('touch file')


@pun.task()
def remove_cd():
    """
    Remove file in current directory.
    """

    with pun.cd('./tests'):
        pun.run('rm file')


@pun.task()
def fail():
    """
    Test failed stat.
    """

    1 / 0


@pun.task()
def default():
    """
    This should executed when no arg.
    """

    pun.run('echo default')
