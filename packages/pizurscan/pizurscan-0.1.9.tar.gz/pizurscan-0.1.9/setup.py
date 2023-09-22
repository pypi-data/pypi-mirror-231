from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pizurscan",
    version="0.1.9",
    description="Library to interface PI controllers and Zurich lock-in",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pizur-scanner.readthedocs.io/",
    author="Giacomo Rizzi",
    author_email="rizzigiacomo@pm.me",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows"
    ],
    packages=["pizurscan"],
    include_package_data=True,
    install_requires=["numpy"]
)