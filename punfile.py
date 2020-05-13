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


@pun.task()
def docs():
    """
    Generate Sphinx HTML documentation, including API docs.
    """

    pun.run("rm -f docs/pun.rst")
    pun.run("rm -f docs/modules.rst")
    pun.run("sphinx-apidoc -o docs/ pun")

    with pun.cd('./docs'):
        pun.run("make clean")
        pun.run("make html")

    pun.run(browser, "docs/_build/html/index.html")


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
@pun.task(hide=True)
def touch():
    """
    Create file in current directory.
    """

    pun.run('touch file')


@pun.task(hide=True)
def remove():
    """
    Remove file in current directory.
    """

    pun.run('rm file')


@pun.task(hide=True)
def touch_cd():
    """
    Create file in current directory.
    """

    with pun.cd('./tests'):
        pun.run('touch file')


@pun.task(hide=True)
def remove_cd():
    """
    Remove file in current directory.
    """

    with pun.cd('./tests'):
        pun.run('rm file')


@pun.task(hide=True)
def fail():
    """
    Test failed stat.
    """

    1 / 0


@pun.task(hide=True)
def default():
    """
    This should executed when no arg.
    """

    pun.run('echo default')


@pun.fixture
def one():
    """
    Return int 1.
    """

    return 1


@pun.fixture
def two():
    """
    Return int 2.
    """

    return 2


@pun.fixture
def three():
    """
    Return int 3.
    """

    return 3


@pun.fixture
def four():
    """
    Return int 4.
    """

    return 4


@pun.task(hide=True)
def need_fixture1(one):
    """
    This task need one fixture.
    """

    pun.run(print, one())


@pun.task(hide=True)
def need_fixture2(one, two):
    """
    This task need two fixture.
    """

    pun.run(print, one() + two())


@pun.task(hide=True)
def need_fixture3(one, two, three):
    """
    This task need three fixture.
    """

    pun.run(print, one() + two() + three())


@pun.task(hide=True)
def need_fixture4(one, two, three, four):
    """
    This task need three fixture.
    """

    pun.run(print, one() + two() + three() + four())


@pun.task(hide=True)
def no_fixture(undefined):
    """
    Fail because no fixture named 'undefined'.
    """

    pun.run(print, undefined())


@pun.task(hide=True)
def punned_fixture(punned):
    """
    Fail because no fixture named 'undefined'.
    """

    pun.run(print, punned)
