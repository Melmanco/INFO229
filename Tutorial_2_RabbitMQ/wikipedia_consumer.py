import pika
import sys
import wikipedia

# Get summary of wikipedia search
def callback(ch, method, properties, body):
    query = body.decode()

    print(' [Wikipedia Search] {} result:\n '.format(query) +
            wikipedia.summary(query) +
          '\n\n\n [Wikipedia Search] Waiting. To exit press CTRL+C')

def main():
    wikipedia.set_lang("es")

    # RabbitMQ setup
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_querys', exchange_type='direct')

    wiki_queue = channel.queue_declare(queue='', exclusive=True)
    queue_name = wiki_queue.method.queue

    channel.queue_bind(exchange='direct_querys', queue=queue_name, routing_key='wikipedia')

    # Ready to consume
    print(' [Wikipedia Search] Waiting. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    main()