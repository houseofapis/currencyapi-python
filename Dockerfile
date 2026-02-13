FROM python:3.14-alpine

WORKDIR /app

RUN pip install requests \
                coverage \
                twine \
                wheel \
                setuptools
