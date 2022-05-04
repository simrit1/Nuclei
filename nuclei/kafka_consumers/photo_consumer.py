from kafka import KafkaConsumer, KafkaProducer
import os
import json
import uuid
from concurrent.futures import ThreadPoolExecutor

TOPIC_NAME = "PHOTO"
consumer = KafkaConsumer(
    TOPIC_NAME,
    # to deserialize kafka.producer.object into dict
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)


def sendNotification(data):
    """
    . . . . .
        . . . . .
        . . . . .
        process steps
        . . . . .
        . . . . .
    """


for notification in consumer:

    notification_data = email.value

    sendNotification(notification_data)