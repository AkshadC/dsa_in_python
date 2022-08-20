from queue_implementation import Queue


def print_binary1(n):
    start = 1
    numbers = Queue()
    numbers.enqueue(start)
    temp = []
    cnt = 1
    while cnt < n+1:
        front = numbers.dequeue()
        elem1 = str(front) + "0"
        elem2 = str(front) + "1"
        numbers.enqueue(elem1)
        numbers.enqueue(elem2)
        cnt += 1
        temp.append(front)
    print(temp)


def print_binary2(n):
    numbers = Queue()
    numbers.enqueue("1")
    print("[", end=" ")
    for i in range(n):
        front = numbers.get_first_out_element()
        print(" ", front, end=" ")
        numbers.enqueue(front + "0")
        numbers.enqueue(front + "1")
        numbers.dequeue()
    print("]")


if __name__ == "__main__":
    print_binary1(10)
    print_binary2(10)
