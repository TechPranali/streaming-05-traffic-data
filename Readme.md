# Real-Time Traffic Data Analysis with RabbitMQ

## Project Overview
This project showcases a real-time streaming analytics solution using RabbitMQ, Python, and Faker. The primary goal is to simulate real-time traffic data, stream it using RabbitMQ, process the incoming data with Python, and visualize the results. This project demonstrates the implementation of custom producers and consumers for streaming data and explores the use of RabbitMQ exchanges and queues.

## Data Source
The data used in this project is entirely simulated using the Faker library. Faker generates realistic data such as street names and vehicle counts to mimic real-world traffic data.

## Implementation Details

### Producers
The producer script (`producer.py`) simulates real-time traffic data and sends it to a RabbitMQ exchange. The data includes a timestamp, a location (street name), and a vehicle count. Here’s how the producer works:
- Establishes a connection to the RabbitMQ server.
- Declares an exchange named `traffic`.
- Generates traffic data using Faker.
- Publishes the data to the `traffic` exchange.

### Consumers
The consumer script (`consumer.py`) receives traffic data from the RabbitMQ exchange, processes it, and visualizes it. Here’s how the consumer works:
- Establishes a connection to the RabbitMQ server.
- Declares an exchange named `traffic` and binds a queue named `traffic_data` to it.
- Processes incoming messages, collects data, and visualizes it using Matplotlib.

### Exchanges and Queues
- **Exchange**: `traffic` (type: direct)
- **Queue**: `traffic_data`

### Running the Project

#### Step 1: Start the RabbitMQ Server
Ensure the RabbitMQ server is running on your local machine. You can start it using the command:
rabbitmq-server

#### Step 2: Run the Producer
Open a terminal and run the producer.py script:

python producer.py

#### Step 3: Run the Consumer
Open another terminal and run the consumer.py script:

python consumer.py


### Producer Consumer Console Output

![The Producer Consumer Console](<images/Producer Consumer Console Output.png>)

### Graph Visualization

- The graph will visualize the real-time traffic data:

- **X-axis** (Time): The time at which the traffic data was received.
- **Y-axis** (Vehicle Count): The number of vehicles counted at each location and time.

![Graphical Representation of Trafic Data](<images/Graphical Representation of Trafic Data.png>)