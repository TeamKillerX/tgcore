import os
import re

import setuptools


def read(fname, version=False):
    path = os.path.join(os.path.dirname(__file__), fname)
    text = open(path, encoding="utf8").read()
    return re.search(r'__version__ = "(.*?)"', text)[1] if version else text

setuptools.setup(
    name="tgcore",
    packages=setuptools.find_packages(),
    version=read("tgcore/__version__.py", version=True),
    license="Apache-2.0",
    description="TGCoreSDK | Enterprise Telegram Bot API Framework.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="TeamKillerX",
    project_urls={
        "Source": "https://github.com/TeamKillerX/tgcore",
        "Issues": "https://github.com/TeamKillerX/tgcore/issues",
        "Documentation": "https://services-pro.ryzenths.dpdns.org/api/v2/docs"
    },
    keywords=[
        "telegram",
        "telegram-bot",
        "telegram-api",
        "sdk",
        "framework",
        "tgcore",
        "ryzenth"
    ],
    install_requires=[
        "httpx>=0.24.0"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
)
