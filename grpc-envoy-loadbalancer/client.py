import grpc
import msg_schema_pb2
import msg_schema_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = msg_schema_pb2_grpc.GreeterStub(channel)
        print('here')
        print(stub)
        response = stub.SayHello(msg_schema_pb2.HelloRequest(name='World'))
        print(response)

run()