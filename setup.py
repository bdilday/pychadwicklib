from skbuild import setup
from setuptools import find_packages

import pathlib
import os


setup(
    name="pychadwicklib",
    version="0.1.0",
    description="pychadwicklib",
    author="Ben Dilday",
    author_email="ben.dilday.phd@gmail.com",
    url="https://github.com/bdilday/pychadwicklib",
    packages=find_packages(),
    cmake_install_dir="pychadwicklib/lib",
)
