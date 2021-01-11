FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestorbot.py /nestorbot.py

CMD [ "python", "/nestor_slack_writer.py" ]
