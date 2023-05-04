import grpc
import msg_schema_pb2
import msg_schema_pb2_grpc
import postgres_pb2
import postgres_pb2_grpc

def run():
    # Connect to the server
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = msg_schema_pb2_grpc.GreeterStub(channel)
        print(stub)
        print(msg_schema_pb2.HelloRequest(name='World'))
        response = stub.SayHello(msg_schema_pb2.HelloRequest(name='World'))
        print(response)

        stub = postgres_pb2_grpc.PostgresServiceStub(channel)
        print(stub)
        response = stub.ExecuteQuery(postgres_pb2.QueryRequest(query='SELECT * FROM test'))
        print(response)

run()