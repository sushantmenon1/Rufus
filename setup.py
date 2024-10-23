from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Implementation of the RuFus Agent'
LONG_DESCRIPTION = 'A package that allows to build a RAG Agent that scrapes websites dynamically.'

# Setting up
setup(
    name="rufus",
    version=VERSION,
    author="Sushant Menon",
    author_email="sushantmenon1@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
    "langchain==0.3.4",
    "langchain-openai==0.2.3",
    "fastapi==0.115.3",
    "pydantic==2.9.2",
    "openai==1.52.0",
    "xmltodict==0.14.2",
    "beautifulsoup4==4.12.3",
    "langchain_core==0.3.12"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)