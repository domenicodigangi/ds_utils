#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["numpy>=1.19", "pandas>=1.2", "scipy>=1.6" "torch"]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Domenico Di Gangi",
    author_email="digangidomenico@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="utils for data science projects",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords="ds_utils",
    name="ds_utils",
    packages=find_packages(include=["ds_utils", "ds_utils.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    version="0.1.0",
    zip_safe=False,
)
