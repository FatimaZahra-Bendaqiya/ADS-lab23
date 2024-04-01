class Stack:
    def __init__(self, size, data_type):
        self.size = size
        self.stack = []
        self.data_type = data_type
        self.top_index = -1

    def push(self, element):
        if self.top_index + 1 >= self.size:
            print("The stack is full.")
        else:
            self.top_index += 1
            self.stack.append(element)

    def pop(self):
        if self.top_index == -1:
            return None
        else:
            self.top_index -= 1
            return self.stack[self.top_index + 1]

    def is_empty(self):
        if self.top_index == -1:
            return True
        return False

    def top(self):
        if self.top_index == -1:
            return None
        else:
            return self.stack[self.top_index]

    def print_stack(self):
        print(self.stack[0:self.top_index + 1])


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, element):
        if self.size == 0:
            self.head = self.tail = Node(element)
        else:
            self.tail.next = Node(element)
            self.tail = self.tail.next
        self.size += 1

    def remove_first(self):
        if self.size == 0:
            return None
        else:
            temp_node = self.head
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return temp_node.value

    def get_first(self):
        if self.size == 0:
            return None
        else:
            return self.head.value

    def get_size(self):
        return self.size


def add_nodes_to_sll(sll, user_input):
    for i in range(len(user_input)):
        sll.add_node(user_input[i])


def add_elements_to_stack(stack, user_input):
    for i in range(len(user_input)):
        stack.push(user_input[i])


def check_palindrome(first_half, second_half):
    for _ in range(first_half.size):
        if first_half.remove_first() != second_half.pop():
            return "This is not a palindrome"
    return "This is a palindrome"


input_palindrome = input()

first_half = SinglyLinkedList()
second_half = Stack(100, str)

add_nodes_to_sll(first_half, input_palindrome[0:len(input_palindrome) // 2])
add_elements_to_stack(second_half, input_palindrome[len(input_palindrome) -
                                                    len(input_palindrome) // 2:len(input_palindrome)])

print(check_palindrome(first_half, second_half))
