import pika
import urllib
import urllib.request
import re

# Message receive and youtube search using http request and regular expressions
def callback(ch, method, properties, body):
    query = urllib.parse.quote(body.decode('utf8'))

    try:

        html = urllib.request.urlopen('https://www.youtube.com/results?search_query={}'.format(query))
        video_id = re.search(r"watch\?v=(\S{11})", html.read().decode()).group(0)
        video_link = 'https://www.youtube.com/{}'.format(video_id)

        print(' [Youtube Search] result:\n' +
              ' {}\n'.format(video_link))

    except urllib.error.HTTPError as HTTPError:
        print('Error {}: {}'.format(HTTPError, HTTPError.message))

def main():
    # RabbitMQ setup
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_querys', exchange_type='direct')

    youtube_queue = channel.queue_declare(queue='', exclusive=True)
    queue_name = youtube_queue.method.queue

    channel.queue_bind(exchange='direct_querys', queue=queue_name, routing_key='youtube')

    # Ready to consume
    print(' [Youtube Search] Waiting. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    main()