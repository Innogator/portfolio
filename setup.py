#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import portfolio
version = portfolio.__version__

setup(
    name='portfolio',
    version=version,
    author='',
    author_email='btanne6@gmail.com',
    packages=[
        'portfolio',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['portfolio/manage.py'],
)
