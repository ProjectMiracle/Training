import time
import grpc
from proto import message_pb2
from proto.message_pb2 import QuestionType, Instance, QuestionRequest


def gen():
    while 1:
        i = input("\nEnter a number or 'q' to quit: \n")
        if i == "q":
            break
        try:
            num = i
        except ValueError:
            continue
        yield message_pb2.QuestionRequest(Instance(1))
        time.sleep(0.1)


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = message_pb2.SolverServiceStub(channel)
    it = stub.AnswerQuestion(message_pb2.QuestionRequest(question=Instance(question='a b e i d')))

    try:
        for r in it:
            print("{r.result}")
    except grpc._channel._Rendezvous as err:
        print(err)


if __name__ == '__main__':
    run()
