FROM python:3.9.1

ARG SLACK_TOKEN

ENV SLACK_TOKEN         $SLACK_TOKEN
ENV MONGO_HOST          localhost
ENV MONGO_PORT          "mongodb://mongo:27017/"


COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./jamesbot_app.py /jamesbot_app.py
COPY ./jamesbot.py /jamesbot.py

CMD [ "python", "/jamesbot_app.py"]