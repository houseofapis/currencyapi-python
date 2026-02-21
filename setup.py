from setuptools import setup, find_packages
from os.path import abspath, dirname, join

with open(join(dirname(abspath(__file__)), "README.md")) as f:
    README_MD = f.read()

setup(
    name="currencyapinet",
    version="2.0.0",
    packages=find_packages(exclude="tests"),
    description="Python wrapper for CurrencyApi.net",
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://currencyapi.net/sdk/python",
    author="Oli Girling",
    author_email="support@currencyapi.net",
    python_requires=">=3.10",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "requests"
    ],
    keywords="currency feed, currency rates, currencyapi, currency",
)
