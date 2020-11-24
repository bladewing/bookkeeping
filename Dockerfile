# pull official base image
FROM python:3.9.0-alpine

# set work directory
WORKDIR /usr/src/bookkeeping

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .
RUN chmod +x /usr/src/bookkeeping/entrypoint.sh

ENTRYPOINT ["/usr/src/bookkeeping/entrypoint.sh"]