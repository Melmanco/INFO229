import os
import pika
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from nestorbot import NestorBot

HOST = os.environ['RABBITMQ_HOST']

# On slack message, process message and sends to nestor_events
@slack_events_adapter.on('message')
def message(payload):

    # Command parse
    event = payload.get('event, {}')
    text = event.get().lower()
    (command, args) = text.split(' ', maxsplit=1)
    prefix = command.pop(0)
    command = command.pop(0)

    # RabbitMQ setup
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    if prefix == 'nestor':
        if command == 'wikipedia' or command == 'translate':

            # Sends message to nestor_events, with exchange 'read'
            # and routing_key 'wikipedia' or 'translate'
            channel.exchange_declare(exchange='read', exchange_type='direct')
            channel.basic_publish(exchange='read', routing_key=command, body=args)
            
            print(" [x] Sent {}: {}".format(command, args))

        else:
            usage_error = 'Usage: nestor_slack_reader.py [wikipedia | translate] [ | language] [search | sentence]'

            nestor_bot = NestorBot("bot")
            message = nestor_bot.get_message_payload(usage_error)
            slack_web_client.chat_postMessage(**message)

        connection.close()

if __name__ == '__main__':
    app = Flask(__name__)
    slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)
    slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))
    app.run(host='0.0.0.0', port=3000)