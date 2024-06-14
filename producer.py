# producer.py

import pika
import json
import time
from faker import Faker

# Initialize Faker
fake = Faker()

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare an exchange
channel.exchange_declare(exchange='traffic', exchange_type='direct')

def generate_traffic_data():
    """
    Generate random traffic data using Faker.
    Returns:
        str: JSON string of traffic data including timestamp, location, and vehicle count.
    """
    traffic_data = {
        'timestamp': time.time(),
        'location': fake.street_name(),
        'vehicle_count': fake.random_int(min=0, max=50)
    }
    return json.dumps(traffic_data)

# Continuously send traffic data to the exchange
while True:
    traffic_data = generate_traffic_data()
    channel.basic_publish(exchange='traffic',
                          routing_key='traffic_data',
                          body=traffic_data)
    print(f"Sent: {traffic_data}")
    time.sleep(1)  # Wait for 1 second before sending the next data

# Close the connection
connection.close()