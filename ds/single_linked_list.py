class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_element(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_list(self):
        if self.is_list_empty():
            print("THE LIST IS EMPTY")
            return
        start = self.head

        while start:
            print(start.data, "->", end=" ")
            start = start.next_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        start = self.head
        while start.next_node:
            start = start.next_node

        node_new = Node(data)
        start.next_node = node_new

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            node = Node(data, self.head)
            self.head = node

    def is_list_empty(self):
        return self.head is None

    def create_linked_list(self, data_list):
        self.head = None
        for d in data_list:
            self.insert_at_end(d)

    def get_length_list(self):
        start = self.head
        itr = 0
        while start:
            itr += 1
            start = start.next_node
        return itr

    def remove_node_at(self, index):
        if index < 0 or index > self.get_length_list():
            raise Exception("INDEX OUT OF BOUNDS")

        if index == 0:
            self.head = self.head.next_node
            return

        start = self.head
        itr = 0
        while start:
            if itr == index - 1:
                start.next_node = start.next_node.next_node
                break
            start = start.next_node
            itr += 1

    def insert_node_at(self, index, data):
        if index < 0 or index > self.get_length_list():
            raise Exception("INDEX OUT OF BOUNDS")

        if index == 0:
            node1 = Node(data)
            node1.next_node = self.head
            return
        start = self.head
        count = 0
        while start:
            if count == index - 1:
                node = Node(data, start.next_node)
                start.next_node = node
                break
            count += 1

    def insert_data_after_value(self, data_after, data_to_insert):
        if self.is_list_empty():
            return "THE LIST IS EMPTY"
        if self.is_data_in_ll(data_after):

            start = self.head
            while start:
                if start.data == data_after:
                    start.next_node = Node(data_to_insert, start.next_node)
                    break
                start = start.next_node

    def remove_by_value(self, data):
        if self.is_list_empty():
            return "THE LIST IS EMPTY"
        start = self.head
        while start.next_node:
            if start.next_node.data == data:
                start.next_node = start.next_node.next_node
                break
            start = start.next_node

    def is_data_in_ll(self, data):
        if self.is_list_empty():
            return False
        start = self.head
        while start:
            if start.data == data:
                return True
            start = start.next_node
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_element(6)
    ll.insert_element(416)
    ll.insert_element(146)
    ll.insert_element(6213)
    ll.insert_element(61)
    ll.insert_at_end(3)
    ll.print_list()
