==============
Advanced usage
==============

Required
--------

Sometime one task need to run another task, example: A deploy task need to run
build task before executing itself.

The ``@pun.task()`` decorator accept many argument of required task. It can be
``str`` or an instance of ``Task`` (a function decorated with ``@pun.task()``).

.. code-block:: python

    import pun


    # this build task is required for deploy
    @pun.task()
    def build():
        """
        Builds source and wheel package.
        """

        pun.run("python setup.py sdist")
        pun.run("python setup.py bdist_wheel")


    # We provide the required task
    # as an argument in ``task`` decorator
    @pun.task('build')
    def deploy():
        """
        Upload final release.
        """

        pun.run('twine upload dist/*')


Change working directory
------------------------

.. code-block:: python

    import pun


    @pun.task()
    def docs():
        """
        Generate Sphinx HTML documentation, including API docs.
        """

        pun.run("rm -f docs/pun.rst")
        pun.run("rm -f docs/modules.rst")
        pun.run("sphinx-apidoc -o docs/ pun")

        # Change working directory to ./docs
        # to run a command in that directory
        with pun.cd('./docs'):
            pun.run("make clean")
            pun.run("make html")
