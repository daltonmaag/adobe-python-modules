#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name = "adobe-type-tools-modules",
    version = "0.1",
    description = "Adobe type tools Python modules.",
    author = "Frank Grießhammer,  Miguel Sousa, others",
    # email = "",
    url = "https://github.com/adobe-type-tools/python-modules",
    py_modules = [
        "WriteFeaturesKernFDK",
        "WriteFeaturesMarkFDK",
    ],
)
