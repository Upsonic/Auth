#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="upsonic_auth",
    version="0.2.0",
    description="""The cloud authentication save system for your python applications !""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/Upsonic/Upsonic-Auth",
    author="Onur Atakan ULUSOY",
    author_email="atadogan06@gmail.com",
    license="MIT",
    packages=["upsonic_auth",],
    install_requires=install_requires,
    python_requires=">= 3",
    zip_safe=False,
)

