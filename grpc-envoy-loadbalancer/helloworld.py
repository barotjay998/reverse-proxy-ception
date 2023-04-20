from concurrent import futures
import grpc
import msg_schema_pb2

import msg_schema_pb2_grpc

class Greeter(msg_schema_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print('request received')
        print(request)
        #TODO: forward to kafka
        print('forward to kafka')
        return msg_schema_pb2.HelloReply(message=f'Hello, {request.name}!')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    msg_schema_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('server started')
    server.wait_for_termination()
    print('server terminated')

if __name__ == '__main__':
    serve()
