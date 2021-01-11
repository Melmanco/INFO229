FROM python:3.6.3

ENV SLACK_TOKEN     xoxb-1419412195043-1488045592838-05xkZGQvhD0ommm26mgRJN9k

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]