import json
import os

from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError
from dotenv import load_dotenv

load_dotenv()

kafka_brokers = os.environ.get('KAFKA_BROKERS')

def sendData(topic_name, data, metadata = {}):
    producer = None
    try:
        error = ''
        producer = KafkaProducer(bootstrap_servers=kafka_brokers)
        input = {
            'data': data,
            'id': metadata['id'] if 'id' in metadata else '',
            'source': metadata['trigger_source'] if 'trigger_source' in metadata else 'none'
        }
        message_value = json.dumps(input).encode('utf-8')
        ack = producer.send(topic_name, value=message_value)
        return ack.get()
    except KafkaTimeoutError as e:
        error = f'Timeout error in sending data to kafka topic {topic_name}'
        raise error
    except Exception as e:
        error = f'An error occured in sending data to kafka topic {topic_name}'
        raise error
    finally:
        if producer is not None:
            producer.close()
