FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_malla

COPY ./nestor_malla.py /nestor_malla.py

CMD [ "python", "/nestor_malla.py" ]