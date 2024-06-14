# consumer.py

import pika
import json
import pandas as pd
import matplotlib.pyplot as plt

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare an exchange and a queue
channel.exchange_declare(exchange='traffic', exchange_type='direct')
channel.queue_declare(queue='traffic_data')
channel.queue_bind(exchange='traffic', queue='traffic_data', routing_key='traffic_data')

traffic_data_list = []

def callback(ch, method, properties, body):
    """
    Callback function to process received messages.
    Args:
        ch: Channel
        method: Method
        properties: Properties
        body: Message body (traffic data)
    """
    data = json.loads(body)
    traffic_data_list.append(data)
    print(f"Received: {data}")

    if len(traffic_data_list) >= 10:
        df = pd.DataFrame(traffic_data_list)
        plt.figure(figsize=(10, 5))
        plt.plot(pd.to_datetime(df['timestamp'], unit='s'), df['vehicle_count'])
        plt.xlabel('Time')
        plt.ylabel('Vehicle Count')
        plt.title('Real-Time Traffic Data')
        plt.show()
        traffic_data_list.clear()

channel.basic_consume(queue='traffic_data',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()