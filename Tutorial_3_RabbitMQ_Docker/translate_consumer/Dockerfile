FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /trasnlate_consumer

COPY ./translate_consumer.py /translate_consumer.py

CMD [ "python", "/translate_consumer.py" ]
