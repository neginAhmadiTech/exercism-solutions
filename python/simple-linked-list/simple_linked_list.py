class EmptyListException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next

    def set_next(self, next):
        self._next = next


class LinkedList:
    def __init__(self, values=None):
        self._length = 0
        self._head = None

        if values is None:
            return

        for item in values:
            self.push(item)

    def __iter__(self):
        current = self._head

        while current is not None:
            yield current.value()
            current = current.next()

    def __len__(self):
        return self._length

    def head(self):

        if self._head is None:
            raise EmptyListException("The list is empty.")

        return self._head

    def push(self, value):
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
            self._length += 1
            return

        new_node.set_next(self._head)
        self._head = new_node
        self._length += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")

        value = self._head.value()
        self._head = self._head.next()
        self._length -= 1

        return value

    def reversed(self):

        previous = None
        current = self._head

        while current is not None:
            next_node = current.next()  # remember where we're going
            current.set_next(previous)  # reverse the arrow

            previous = current  # move previous forward
            current = next_node  # move current forward

        self._head = previous

        return iter(self)
