from setuptools import setup, find_packages

long_description = """
Kafkawrapper
================

KafkaWrapper is a Python library designed to simplify Kafka producer setup and data transmission to Kafka topics. This wrapper abstracts the complexities of configuring a Kafka broker and producer, allowing developers to seamlessly integrate Kafka into their projects.

Features
--------

- KafkaWrapper simplifies the process of setting up a Kafka broker and producer, saving you time and effort.
- asily send data to Kafka topics without the need for extensive Kafka knowledge.
- Customize your Kafka producer settings to suit your specific use case.

Usage
-----

To send data to Kafka, follow these steps:

1. Import the `sendData` modules.
2. Use this module to send data to kafka.
3. Argument are 
   kafka_topic: Topic name
   data: that you want to send to kafka
   metadata(optional): id - unique id to fetch particular record from kafka

License
-------

This project is licensed under the MIT License.
"""

setup(
    name='kafkawrapper',
    version='1.0.1',
    description='A wrapper for Kafka producer',
    author='Pradeep',
    author_email='pradeep@incaendo.com',
    packages=find_packages(),
    install_requires=[
        'kafka-python==2.0.2',
    ],
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/x-rst'
)