"""
    Kafka Producer Base Class - Public Transport Optimisation
    Used for creating a Producer with basic functionality
"""

import logging
import time

from confluent_kafka import avro
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroProducer

logger = logging.getLogger(__name__)

class Producer:
    """ Defines and provides common functionality amongst Producers """

    # Tracks existing topics across all Producer instances
    existing_topics = set([])

    def __init__(
        self,
        topic_name,
        key_schema,
        value_schema=None,
        num_partitions=1,
        num_replicas=1,
    ):

        """ Initialises a Producer object with basic settings """
        self.topic_name = topic_name
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.num_partitions = num_partitions
        self.num_replicas = num_replicas

        self.broker_properties = {
            # Add properties here
        }

        # If the topic does not already exist, try to create it
        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        self.producer = AvroProducer(
            # Add properties here
        )

    def create_topic(self):
        """ Creates the producer topic if it does not already exist """
        # Add code here

    def close(self):
        """ Prepares the producer for exit by cleaning up the producer """
        # Add code here

    def time_millis(self):
        """ Use this function to get the key for Kafka Events """
        return int(round(time.time() * 1000))
