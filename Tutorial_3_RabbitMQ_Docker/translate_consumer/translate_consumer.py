import pika
import os
import transformers
from transformers import pipeline
from transformers import AutoModelWithLMHead, AutoTokenizer, MarianTokenizer, MarianMTModel

HOST = os.environ['RABBITMQ_HOST']

# Reply with translated sentence to nestor_events
def on_request(ch, method, props, body):
    query = body.decode()
    to_translate = [query]

    translated = model.generate(**tokenizer.prepare_translation_batch(to_translate))
    result = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

    print(' [Translated] {}\n'.format(query))

    ch.basic_publish(exchange=method.exchange,
                     routing_key='translate',
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id
                     ),
                     body=result)
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':

    # transformers setup
    model_name = "Helsinki-NLP/opus-mt-es-en"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # RabbitMQ setup
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    result = channel.queue_declare(queue='')
    queue_name = result.method.queue

    # Ready to consume
    print(' [Translate] Waiting. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=on_request, auto_ack=True)

    channel.start_consuming()