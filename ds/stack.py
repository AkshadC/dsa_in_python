from collections import deque


def reverse_string(string):
    stack1 = Stack()
    for s in string:
        stack1.push(s)
    rev_string = ""
    for i in range(stack1.size()):
        rev_string += stack1.pop()
    return rev_string


def check_matching_paren(p1, p2):
    parenthesis_dict = {')': '(', ']': '[', '>': '<', '}': '{'}
    return parenthesis_dict[p1] == p2


def balanced_parenthesis_check(string):
    stack = Stack()
    for s in string:
        if s in ['(', '{', '[', '<']:
            stack.push(s)
        if s in [')', '}', ']', '>']:
            if stack.size() == 0:
                return False
            if not check_matching_paren(s, stack.pop()):
                return False
    return stack.size() == 0


class Stack:

    def __init__(self):
        self.box = deque()

    def pop(self):
        if self.is_empty():
            raise Exception("THE STACK IS EMPTY")
        return self.box.pop()

    def push(self, data):
        self.box.append(data)

    def peek(self):
        if self.is_empty():
            raise Exception("THE STACK IS EMPTY")
        return self.box[-1]

    def is_empty(self):
        return len(self.box) == 0

    def size(self):
        return len(self.box)


if __name__ == "__main__":
    print(reverse_string("AKSHAD CHIDRAWAR"))
    print(balanced_parenthesis_check("(hello[my {name is [fasf]{sfaf}]2gas})"))