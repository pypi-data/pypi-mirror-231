#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "aim-platform-sdk>=0.1.3",
    "docker>=4.2.2",
    "aim-git-util>=0.1.1",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="AI Maintainer Inc",
    author_email="douglas@ai-maintainer.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="AI Maintainer Agent Harness for our benchmarking and Marketplace API and platform",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="coder_evals",
    name="coder_evals",
    packages=find_packages(include=["coder_evals"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/ai-maintainer-inc/coder-evals",
    # fmt: off
    version='0.1.3',
    # fmt: on
    zip_safe=False,
)
