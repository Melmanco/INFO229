import pika
import sys

def main(argv):

    # CLI arguments 
    usage_error = 'Usage: producer.py [wikipedia | youtube] search'

    if len(argv) < 2:
        print(usage_error)
        return

    web = argv[0].lower()
    if web not in ('wikipedia', 'youtube'):
        print(usage_error)
        return

    search = ' '.join(argv[1:])

    # RabbitMQ setup
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_querys', exchange_type='direct')
    channel.basic_publish(exchange='direct_querys', routing_key=web, body=search)
    
    print(" [x] Sent {}: {}".format(web, search))

    connection.close()

if __name__ == '__main__':
    main(sys.argv[1:])