# pull official base image
FROM python:3.9.6-slim
ENV DEBIAN_FRONTEND noninteractive
ARG REPO_PATH
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install dialog -y
RUN apt-get install apt-utils -yq
RUN apt-get install gcc -y
# Install Postgres
RUN apt-get install libpq-dev -y
# install netcat : for the nc command in entrypoin.sh
RUN apt-get install -y netcat

# set the working directory
RUN mkdir app
WORKDIR /app
# copy project
COPY $REPO_PATH /app


# copy and install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]