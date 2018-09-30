#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup script for spyder-black."""

import os
import os.path as osp

from setuptools import find_packages, setup


def get_version():
    """Get the version."""
    with open("spyder_black/__init__.py") as f:
        lines = f.read().splitlines()
        for l in lines:
            if "__version__" in l:
                version = l.split("=")[1].strip()
                version = version.replace("'", "").replace('"', "")
                return version


def get_readme():
    """Get the README."""
    with open("README.rst") as f:
        readme = str(f.read())
    return readme


def get_package_data(name, extlist):
    """Return data files for package *name* with extensions in *extlist*."""
    flist = []
    # Workaround to replace os.path.relpath (not available until Python 2.6):
    offset = len(name) + len(os.pathsep)
    for dirpath, _dirnames, filenames in os.walk(name):
        for fname in filenames:
            if not fname.startswith(".") and osp.splitext(fname)[1] in extlist:
                flist.append(osp.join(dirpath, fname)[offset:])
    return flist


# Requirements
REQUIREMENTS = ["black"]
EXTLIST = [".jpg", ".png", ".json", ".mo", ".ini"]
LIBNAME = "spyder-black"


setup(
    name=LIBNAME,
    version=get_version(),
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    package_data={LIBNAME: get_package_data(LIBNAME, EXTLIST)},
    keywords=["Qt PyQt4 PyQt5 PySide spyder plugins spyplugins black"],
    install_requires=REQUIREMENTS,
    url="https://github.com/jeverling/spyder-black",
    license="MIT",
    author="Jesaja Everling",
    author_email="jeverling@gmail.com",
    maintainer="Jesaja Everling",
    maintainer_email="jeverling@gmail.com",
    description="A plugin to run the black python linter from within Spyder.",
    long_description=get_readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: Qt",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Widget Sets",
    ],
)
