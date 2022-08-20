from collections import deque


class Queue:

    def __init__(self):
        self.my_queue = deque()

    def enqueue(self, data):
        self.my_queue.appendleft(data)

    def dequeue(self):
        if self.is_empty():
            raise Exception("THE QUEUE IS EMPTY")
        return self.my_queue.pop()

    def get_queue_size(self):
        return len(self.my_queue)

    def get_first_out_element(self):
        if self.is_empty():
            raise Exception("THE QUEUE IS EMPTY")
        return self.my_queue[-1]

    def is_empty(self):
        return self.get_queue_size() == 0

    def print_queue(self):
        print("THE QUEUE IS : ", end=" ")
        for i in self.my_queue:
            print(i, end=" ")


if __name__ == "__main__":
    q = Queue()
    q.enqueue(11)
    q.enqueue(1234)
    q.enqueue(9871)
    q.print_queue()
