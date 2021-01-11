FROM python:3.9.1

ARG SLACK_TOKEN

ENV SLACK_TOKEN         $SLACK_TOKEN

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./jamesbot_test.py /jamesbot_test.py
COPY ./jamesbot.py /jamesbot.py

CMD [ "python", "/jamesbot_test.py"]