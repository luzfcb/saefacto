# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import saefacto
version = saefacto.__version__

setup(
    name='saefacto',
    version=version,
    author='',
    author_email='bnafta@gmail.com',
    packages=[
        'saefacto',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['saefacto/manage.py'],
)