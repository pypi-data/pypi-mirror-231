#!/usr/bin/env python3
# Copyright (C) 2015-2023  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from io import open
from os import path

from setuptools import find_namespace_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


def parse_requirements(name=None):
    if name:
        reqf = "requirements-%s.txt" % name
    else:
        reqf = "requirements.txt"

    requirements = []
    if not path.exists(reqf):
        return requirements

    with open(reqf) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            requirements.append(line)
    return requirements


setup(
    name="swh.vault",
    description="Software Heritage vault",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    python_requires=">=3.7",
    author="Software Heritage developers",
    author_email="swh-devel@inria.fr",
    url="https://forge.softwareheritage.org/diffusion/DVAU/",
    packages=find_namespace_packages(include=["swh", "swh.*"]),
    install_requires=parse_requirements() + parse_requirements("swh"),
    setup_requires=["setuptools-scm"],
    use_scm_version=True,
    extras_require={
        "testing": parse_requirements("test"),
        "graph": parse_requirements("swh-graph"),
    },
    include_package_data=True,
    zip_safe=False,
    entry_points="""
        [swh.cli.subcommands]
        vault=swh.vault.cli
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    project_urls={
        "Bug Reports": "https://forge.softwareheritage.org/maniphest",
        "Funding": "https://www.softwareheritage.org/donate",
        "Source": "https://forge.softwareheritage.org/source/swh-vault",
        "Documentation": "https://docs.softwareheritage.org/devel/swh-vault/",
    },
)
