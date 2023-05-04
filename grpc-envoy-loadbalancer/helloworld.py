from concurrent import futures
import grpc
import msg_schema_pb2
import msg_schema_pb2_grpc
import postgres_pb2
import postgres_pb2_grpc
import json
import sqlite3

# Import kafka-python
from kafka import KafkaProducer, KafkaConsumer

class Greeter(msg_schema_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print('request received')
        print(request)

        #TODO: forward to kafka

        return msg_schema_pb2.HelloReply(message=f'Hello, {request.name}!')


class PostgresService(postgres_pb2_grpc.PostgresServiceServicer):

    def execute_query(self, query):
        try:
            print("Executing query : ", query)

            # Create a kafka producer
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

            producer.send('dbquery', {'query': query})

            return [
               ["test_column", "text", "test_value"],
               ["test_column2", "text2", "test_value2"],
            ]
        
        except Exception as e:
            print("Exception occured during query execution : ", e)
            raise e


    def ExecuteQuery(self, request, context):
        print('query request received')
        print(request)

        #TODO: forward to kafka

        # Execute the query and retrieve the results
        try:
            rows = self.execute_query(request.query)

        except Exception as e:
            # If an error occurred, return a QueryResponse object with success=False and an error message
            print("Exception occured during query execution : ", e)
            error_message = str(e)
            return postgres_pb2.QueryResponse(success=False, error=error_message)
        
        else:
            # If the query executed successfully, create a QueryResponse object with success=True and the query results
            query_response = postgres_pb2.QueryResponse(success=True, error='')

            for column_name, data_type, value in rows:      
                row_obj = postgres_pb2.Row() # Allocate a new Row object
                value_obj = postgres_pb2.Value( column_name=column_name, data_type=data_type, value=str(value)) # Allocate a new Value object
                row_obj.values.append(value_obj) # Add the Value object to the Row object
                query_response.rows.append(row_obj) # Add the Row object to the QueryResponse object

            return query_response


def serve():

    # Create the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add the services to the server
    msg_schema_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    postgres_pb2_grpc.add_PostgresServiceServicer_to_server(PostgresService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print('server started')
    server.wait_for_termination()
    print('server terminated')

if __name__ == '__main__':
    serve()
