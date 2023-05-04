import sqlite3
from kafka import KafkaProducer, KafkaConsumer
import json


class DataBaseService():

    def __init__(self):
        # Connect to the database (creates the database if it doesn't exist)
        self.conn = sqlite3.connect('kafkatestdb.db')
        self.bootstrap_servers = ['localhost:9092']
        self.create_table()
        self.create_kafka_consumer('dbquery')

    def create_table(self):
        try:
            print("Creating table")

            # Create a cursor object to execute SQL commands
            c = self.conn.cursor()

            # Create a table
            c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

            # Insert some data into the table
            c.execute("INSERT INTO users VALUES (1, 'Alice', 25)")
            c.execute("INSERT INTO users VALUES (2, 'Bob', 30)")
            c.execute("INSERT INTO users VALUES (3, 'Charlie', 35)")

            # Save the changes to the database
            self.conn.commit()

        except Exception as e:
            print("Error creating table : " + str(e))
    

    def create_kafka_consumer(self, topic):
        try:
            print("Creating kafka consumer")

            # Define the Kafka consumer
            consumer = KafkaConsumer(topic, bootstrap_servers=self.bootstrap_servers,
                                     auto_offset_reset='earliest',
                                     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

            # Consume messages from the Kafka topic
            for message in consumer:
                print("Consumed message")
                print(message.value)
        
        except Exception as e:
            print("Error creating kafka consumer : " + str(e))


if __name__ == '__main__':
    db_service = DataBaseService()