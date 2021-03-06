from skbuild import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="pychadwicklib",
    version="0.3.0",
    author="Ben Dilday",
    author_email="ben.dilday.phd@gmail.com",
    description="Python bindings to the Chadwick library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bdilday/pychadwicklib",
    packages=find_packages(),
    cmake_install_dir="pychadwicklib/lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    install_requires=["scikit-build", "ninja", "cmake", "wheel", "setuptools"],
)
