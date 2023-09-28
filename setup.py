from setuptools import setup, find_packages
from os.path import abspath, dirname, join

README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

setup(
    name="currencyapi",
    version="1.0.0",
    packages=find_packages(exclude="tests"),
    description="Python wrapper for CurrencyApi.net",
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://github.com/houseofapis/currencyapi-python",
    author_name="Oli Girling",
    author_email="support@currencyapi.net",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "requests"
    ],
    keywords="currency feed, currency rates, currencyapi, currency",
)