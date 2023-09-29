FROM python:3-alpine

WORKDIR /app

RUN pip install requests \
                coverage \
                twine \
                wheel
