#!/usr/bin/env python
import pika
import sys
import os
from slack import WebClient
from nestorbot import NestorBot

HOST = os.environ['RABBITMQ_HOST']
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Sends reply from nestor_events to slack
def callback(ch, method, props, body):
    nestor_bot = NestorBot("bot")
    message = nestor_bot.get_message_payload(body.decode())
    slack_web_client.chat_postMessage(**message)

if __name__ == '__main__':

    # RabbitMQ setup
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()
    result = channel.queue_declare(queue='')
    queue_name = result.method.queue
    channel.queue_bind(exchange='write',queue=queue_name)

    # Ready to consume
    channel.basic_consume(queue=queue_name,
                          on_message_callback=callback,
                          auto_ack=True)
