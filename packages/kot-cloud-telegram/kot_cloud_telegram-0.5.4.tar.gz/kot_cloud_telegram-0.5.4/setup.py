#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="kot_cloud_telegram",
    version="0.5.4",
    description="""Hot reload, remote controlled and expandable telegram bot.""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/KOT-database/KOT-Cloud-Telegram",
    cloud_telegramor="Onur Atakan ULUSOY",
    cloud_telegramor_email="atadogan06@gmail.com",
    license="MIT",
    packages=["kot_cloud_telegram",],
    install_requires=install_requires,
    python_requires=">= 3",
    zip_safe=False,
)

