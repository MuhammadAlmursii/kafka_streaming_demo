from confluent_kafka import Producer
import json

me = 'DolZz-1'

conf = {
    'bootstrap.servers': '34.138.205.183:9094,34.138.104.233:9094,34.138.118.154:9094',
    'client.id': me
}

producer = Producer(conf)

def produce_message():
    topic = me
    inp = input('please enter a value: ')
    producer.produce(topic, key=inp, value=inp)
    producer.flush()

if __name__== "__main__":
    produce_message()
