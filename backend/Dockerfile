FROM python:3.6-alpine3.7

RUN apk update && apk add sqlite

RUN apk add build-base python-dev python3-dev py-pip jpeg-dev zlib-dev linux-headers pcre-dev

RUN mkdir /static
RUN mkdir /static/img

RUN mkdir /app
WORKDIR /app

ADD requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD ./ ./
