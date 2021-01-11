import pika
import uuid
import os
HOST = os.environ['RABBITMQ_HOST']

class NestorEvents(object):

    def __init__(self):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='')
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.callback,
            auto_ack=True)

        self.channel.start_consuming()

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

        self.write()

    def write(self):
        self.channel.basic_publish(exchange='write',
                                   routing_key='',
                                   body=self.response)
    
    def call(self, routing_key, body):

        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='{}_process'.format(routing_key),
                              routing_key=routing_key,
                              properties=pika.BasicProperties(
                                  reply_to=self.callback_queue,
                                  correlation_id=self.corr_id
                              ),
                              body=body)
        
        while self.response is None:
            self.connection.process_data_events()
        
        return self.response

    def callback(self, ch, method, properties, body):
        self.response = self.call(method.routing_key, body)

        

if __name__ == '__name__':
    nestor = NestorEvents()