import pika
import wikipedia
import os

HOST = os.environ['RABBITMQ_HOST']

# Reply with summary of wikipedia search to nestor_events
def on_request(ch, method, props, body):
    query = body.decode()
    result = wikipedia.summary(query)

    print(' [Wikipedia Searched] {}\n'.format(query))

    ch.basic_publish(exchange=method.exchange,
                     routing_key='wikipedia',
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id
                     ),
                     body=result)
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':

    # Wikipedia setup
    wikipedia.set_lang("es")

    # RabbitMQ setup
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    wiki_queue = channel.queue_declare(queue='')
    queue_name = wiki_queue.method.queue

    # Ready to consume
    print(' [Wikipedia Search] Waiting. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=on_request, auto_ack=True)

    channel.start_consuming()