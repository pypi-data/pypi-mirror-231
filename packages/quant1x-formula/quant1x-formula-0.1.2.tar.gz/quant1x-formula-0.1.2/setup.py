#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""The setup script."""

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup


def parse_requirements(filename):
    line_iter = (line.strip() for line in open(filename))
    return [line for line in line_iter if line and not line.startswith("#")]


with open("README.rst", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst", encoding="utf-8") as history_file:
    history = history_file.read()

requirements = parse_requirements("requirements.txt")
test_requirements = requirements

from quant1x import __version__, __author__

setup(
    name="quant1x-formula",
    description="Quant1X Formula(python)",
    author_email="wangfengxy@sina.cn",
    url="https://gitee.com/quant1x/formula",
    version=__version__,
    author=__author__,
    long_description=readme,
    packages=find_packages(include=["quant1x", "quant1x.*"]),
    # include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords="quant1x formula",
    entry_points={
        "console_scripts": [
            "quant1x=quant1x.__main__:entry",
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    test_suite="tests",
    tests_require=test_requirements,
    setup_requires=requirements,
)
