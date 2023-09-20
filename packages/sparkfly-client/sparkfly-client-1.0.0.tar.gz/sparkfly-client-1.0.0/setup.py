#!/usr/bin/env python3
from setuptools import setup

from sparkfly_client import __author__, __email__, __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sparkfly-client',
    version=__version__,
    description='A Python client library for Sparkfly',
    long_description=long_description,
    long_description_content_type='text/markdown; charset=UTF-8',
    author=__author__,
    author_email=__email__,
    packages=['sparkfly_client', 'sparkfly_client.api'],
    url='https://github.com/j-madrone/sparkfly',
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'httpx==0.25.0',
        'attrs==21.3.0',
        'python-dateutil==2.8.2'
    ],
)
