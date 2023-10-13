# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Created by: https://www.groundx.ai/
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "groundx-python-sdk"
VERSION = "1.3.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

REQUIRES = [
    "certifi >= 2022.12.7",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.8.2",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
    "validators ~= 0.20.0",]

setup(
    name=NAME,
    version=VERSION,
    description="GroundX API",
    author="Konfig",
    author_email="support@groundx.ai",
    url="https://github.com/groundxai/groundx-sdks/tree/main/sdks/python",
    keywords=["Konfig", "GroundX API"],
    license="MIT",
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
