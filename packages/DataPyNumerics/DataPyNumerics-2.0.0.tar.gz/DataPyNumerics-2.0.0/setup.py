from setuptools import setup, find_packages
import codecs
import os

VERSION = '2.0.0'
DESCRIPTION = 'A tool to help with data, numerics and serialization.'
LONG_DESCRIPTION = 'A tool that will help with data storage, text to numerics and serialization.'

setup(
    name="DataPyNumerics",
    version=VERSION,
    author="chanakya ram sai illa",
    author_email="chanakyaramsaiilla@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['dill'],
    keywords=['numerics', 'datastore', 'serialize'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
