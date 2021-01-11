FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /wikipedia_consumer

COPY ./wikipedia_consumer.py /wikipedia_consumer.py

CMD [ "python", "/wikipedia_consumer.py" ]
