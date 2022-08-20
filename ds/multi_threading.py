import threading
import time

from queue_implementation import Queue

order_queue = Queue()


def place_order(food_orders):
    for o in food_orders:
        print(f"ORDER {o} placed")
        order_queue.enqueue(o)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while True:
        order = order_queue.dequeue()
        print("NOW SERVING :", order)
        time.sleep(2)


if __name__ == "__main__":
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

    t = time.time()
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)
    t1.start()
    t2.start()
