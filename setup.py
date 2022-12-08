#!/usr/bin/env python
from setuptools import setup, find_packages

# Set up the Python module called "knoxnl"
setup(
    name="knoxnl",
    packages=find_packages(),
    version=__import__('knoxnl').__version__,
    description="A Python wrapper around the amazing KNOXSS API by Brute Logic (requires an API Key)",
    long_description=open("README.md").read(),
    author="@xnl-h4ck3r",
    url="https://github.com/xnl-h4ck3r/knoxnl",
    py_modules=["knoxnl"],
    install_requires=["argparse","requests","termcolor"],
)
