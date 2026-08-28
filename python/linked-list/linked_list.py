class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current.value
            current = current.succeeding

    def push(self, node):

        new_node = Node(node)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1

            return

        self.tail.succeeding = new_node
        self.tail.succeeding.previous = self.tail
        self.tail = new_node
        self.length += 1

    def pop(self):

        if self.head is None or self.tail is None or self.length == 0:
            raise IndexError("List is empty")

        value = self.tail.value

        if self.length == 1:
            self.length -= 1
            self.head = None
            self.tail = None

            return value

        self.tail = self.tail.previous
        self.tail.succeeding = None

        self.length -= 1

        return value

    def unshift(self, node):
        new_node = Node(node)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        self.head.previous = new_node
        self.head.previous.succeeding = self.head
        self.head = new_node
        self.length += 1

    def shift(self):

        if self.head is None or self.tail is None or self.length == 0:
            raise IndexError("List is empty")

        value = self.head.value

        if self.length == 1:
            self.length -= 1
            self.head = None
            self.tail = None

            return value

        self.head = self.head.succeeding
        self.head.previous = None

        self.length -= 1

        return value

    def delete(self, node):
        if self.head is None or self.tail is None or self.length == 0:
            raise ValueError("Value not found")

        if self.length == 1 and node == self.head.value:
            self.length -= 1
            self.head = None
            self.tail = None
            return

        current = self.head

        while current.value != node and current.succeeding is not None:
            current = current.succeeding

        if current.succeeding is None and current.value != node:
            raise ValueError("Value not found")

        if current.succeeding is None:
            self.tail = self.tail.previous
            self.tail.succeeding = None
        elif current.previous is None:
            current.succeeding.previous = current.previous
        else:
            current.previous.succeeding = current.succeeding
            current.succeeding.previous = current.previous

        self.length -= 1
