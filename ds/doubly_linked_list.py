class Node:
    def __init__(self, data=None, prev=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_element_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
        else:

            start = self.head
            while start.next_node:
                start = start.next_node
            node = Node(data, start, None)
            start.next_node = node

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            node = Node(data, None, self.head)
            self.head.prev = node
            self.head = node

    def print_list_forward(self):

        if self.head is None:
            print("Linked list is empty")
            return

        start = self.head
        while start:
            print(start.data, "->", end=" ")
            start = start.next_node

    def print_list_backward(self):
        if self.is_list_empty():
            return "THE LIST IS EMPTY"
        end = self.get_last_node()
        while end:
            print(end.data, "<--", end=" ")
            end = end.prev

    def get_last_node(self):
        if self.is_list_empty():
            return "THE LIST IS EMPTY"
        start = self.head
        while start.next_node:
            start = start.next_node
        return start

    def is_list_empty(self):
        return self.head is None

    def get_list_length(self):
        if self.is_list_empty():
            return 0
        count = 0
        start = self.head
        while start:
            count += 1
            start = start.next_node
        return count

    def remove_node_at(self, index):
        if index < 0 or index > self.get_list_length():
            raise Exception("INDEX OUT OF BOUNDS")
        if index == 0:
            self.head = None
        start = self.head
        count = 0
        while start:
            if count == index:
                start.prev.next_node = start.next_node
                if start.next_node:
                    start.next_node.prev = start.prev

            start = start.next_node
            count += 1

    def insert_node_at(self, index, data):
        if index < 0 or index > self.get_list_length():
            raise Exception("INDEX OUT OF BOUNDS")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        start = self.head
        while start:
            if count == index - 1:
                node = Node(data, start, start.next_node)
                if node.next_node:
                    node.next_node.prev = node
                start.next_node = node
                break
            start = start.next_node
            count += 1

    def append_data_list(self, data_list):
        for d in data_list:
            self.insert_element_at_end(d)

    def is_data_in_ll(self, data):
        if self.is_list_empty():
            return False
        start = self.head
        while start:
            if start.data == data:
                return True
            start = start.next_node
        return False

    def add_node_after_node(self, data_after, data):
        if self.is_list_empty():
            return "THE LIST IS EMPTY"

        if self.is_data_in_ll(data_after):
            start = self.head
            while start:
                if start.data == data_after:
                    node = Node(data, start, start.next_node)
                    if node.next_node:
                        node.next_node.prev = node
                    start.next_node = node
                    break
                start = start.next_node


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_element_at_end(1231)
    dll.insert_element_at_end(981)
    dll.insert_at_beginning(9)
    dll.insert_element_at_end(1313)
    dll.insert_node_at(2, 222)
    dll.append_data_list([11, 12, 13, 14, 15])
    dll.add_node_after_node(14, "HELLO THERE")
    dll.print_list_backward()