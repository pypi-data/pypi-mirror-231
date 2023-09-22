#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["click", "cookiecutter", "jinja2"]
test_requirements = ["pytest>=3"]

setup(
    author="drengskapur",
    author_email="service@drengskapur.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="Template ONE gist file. Nothing else! Optional crumbcutter.json for default values.",
    entry_points={
        "console_scripts": [
            "crumbcutter=crumbcutter.cli:main",
        ],
    },
    install_requires=requirements,
    extras_require={
        "dev": ["pytest", "twine", "wheel"],
    },
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="crumbcutter, template, gist",
    name="crumbcutter",
    packages=find_packages(include=["crumbcutter", "crumbcutter.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/drengskapur/crumbcutter",
    version="0.1.9",
    zip_safe=False,
)
