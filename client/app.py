from __future__ import print_function

import logging

import grpc
import users_pb2
import users_pb2_grpc


def run():
    response = []
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.GetUsers(users_pb2.GetUsersRequest())
    print("Users client received: " + str(response.users))


if __name__ == '__main__':
    logging.basicConfig()
    run()