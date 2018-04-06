#!/usr/bin/env python2
from __future__ import print_function
from setuptools import setup

setup(name="enumerate_skip",
      author="Wieland Hoffmann",
      author_email="themineo@gmail.com",
      packages=["enumerate_skip"],
      package_dir={"enumerate_skip": "enumerate_skip"},
      download_url="https://github.com/mineo/enumerate_skip/tarball/master",
      url="http://github.com/mineo/enumerate_skip",
      license="MIT",
      classifiers=["Development Status :: 5 - Production/Stable",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2.6",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
      ],
      description="enumerate extended to support manual advancement or skipping\
      of the index",
      long_description=open("README.rst").read(),
      setup_requires=["setuptools_scm"],
      use_scm_version={"write_to": "enumerate_skip/version.py"},
      )
