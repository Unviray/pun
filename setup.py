#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]


setup(
    author="Unviray",
    author_email='unviray@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description=("Pun mini task to build, deploy or "
                 "anything you like in your project"),
    entry_points={
        'console_scripts': [
            'pun=pun.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pun task tasks task-runner make Makefile',
    name='pun',
    packages=find_packages(include=['pun', 'pun.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Unviray/pun',
    version='0.1.0',
    zip_safe=False,
)
