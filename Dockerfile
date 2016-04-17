FROM python:3.5
MAINTAINER Peter Zhizhin <piter.zh@gmail.com>
RUN apt-get update
RUN apt-get install -y python3-lxml
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
CMD python3 /source/bot_main.py