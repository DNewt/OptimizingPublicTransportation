"""
    Kafka Producer Base Class - Public Transport Optimisation
    Used for creating a Producer with basic functionality
"""

import logging
import time

from confluent_kafka import avro
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroProducer, CachedSchemaRegistryClient

logger = logging.getLogger(__name__)

SCHEMA_REGISTRY_URL = "http://localhost:8081"

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
            "bootstrap.servers": "127.0.0.1:9092"
        }

        # If the topic does not already exist, try to create it
        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        logger.info(f"Creating a new producer for {self.topic_name}")
        self.producer = AvroProducer(
            self.broker_properties,
            schema_registry = CachedSchemaRegistryClient(SCHEMA_REGISTRY_URL),
            default_key_schema = self.key_schema,
            default_value_schema = self.value_schema
        )

    def create_topic(self):
        """ Creates the producer topic if it does not already exist """
        logger.info(f"Creating Topic {self.topic_name}")
        new_topic = []
        new_topic.append(NewTopic(topic=self.topic_name, num_partitions=self.num_replicas, replication_factor=self.num_replicas))

        client = AdminClient({"bootstrap.servers": "127.0.0.1:9092"})
        client.create_topics(new_topic)

    def close(self):
        """ Prepares the producer for exit by cleaning up the producer """
        self.producer.flush()

    def time_millis(self):
        """ Use this function to get the key for Kafka Events """
        return int(round(time.time() * 1000))

