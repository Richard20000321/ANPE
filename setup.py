from setuptools import setup, find_packages
import os

# Read the content of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Define project metadata
setup(
    name="anpe",  # Lowercase package name for PyPI
    version="0.1.0",
    author="Richard",
    author_email="Richard20000321@gmail.com",
    description="Another Noun Phrase Extractor using the Berkeley Neural Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/richard20000321/anpe",
    project_urls={
        "Bug Tracker": "https://github.com/richard20000321/anpe/issues",
        "Documentation": "https://github.com/richard20000321/anpe",
        "Source Code": "https://github.com/richard20000321/anpe",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">=3.9,<3.13",
    install_requires=[
        "spacy>=3.5.0",
        "benepar>=0.2.0",
        "nltk>=3.8.0",
    ],
    entry_points={
        "console_scripts": [
            "anpe=anpe.cli:main",
        ],
    },
    include_package_data=True,
    keywords="nlp, parsing, noun phrase, linguistics, text processing, natural language processing",
    # Add additional package data
    package_data={
        "anpe": ["config/*.py"],
    },
) 