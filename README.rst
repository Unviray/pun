===
Pun
===

.. image:: https://img.shields.io/pypi/v/pun.svg
        :target: https://pypi.python.org/pypi/pun

.. image:: https://img.shields.io/travis/Unviray/pun.svg
        :target: https://travis-ci.org/Unviray/pun

.. image:: https://readthedocs.org/projects/pun/badge/?version=latest
        :target: https://pun.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Pun mini task to build, deploy or anything you like in your project


* Free software: MIT license
* Documentation: https://pun.readthedocs.io.


**In development**


Features
--------

* Run task (of course).
* Run multiple tasks at once
* Run a required task when a task need to run other task
* load a fixture (like in pytest)


Usage
-----

You need a punfile.py to run a task.

To create a sample punfile.py run:

.. code-block:: console

    $ pun init

After ``[ success ] init``, you get you sample punfile.py in your current
directory:

.. code-block:: python

    import pun


    DEFAULT = 'default'


    @pun.task()
    def default():
        """
        Run default action.
        """

        text = "This is a sample punfile (you can edit)"

        pun.run('echo', text)

A task is a function decorated with ``@pun.task()``.

To run this default task, type:

.. code-block:: console

    $ pun default
    $ # or just
    $ pun

We can omit task name (default) because we set ``DEFAULT = 'default'``.

``DEFAULT`` is a variable to handle a default task name to run if we don't
provide a task name in console.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
