FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /events

COPY ./nestor_events.py /nestor_events.py

CMD [ "python", "/nestor_events.py" ]