FROM python:3.8-alpine
MAINTAINER Mohamed Ryad Jeafer

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /code
WORKDIR /code
COPY ./code /code

RUN adduser -D user
USER user