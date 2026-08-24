class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity

        self.read_index = 0
        self.write_index = 0
        self.size = 0

    def read(self):
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")

        read_item = self.buffer[self.read_index]
        self.buffer[self.read_index] = None
        self.read_index = (self.read_index + 1) % self.capacity
        self.size -= 1

        return read_item

    def write(self, data):

        if self.size == self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer[self.write_index] = data
        self.write_index = (self.write_index + 1) % self.capacity
        self.size += 1

    def overwrite(self, data):

        if self.size < self.capacity:
            self.write(data)
            return

        self.buffer[self.write_index] = data
        self.write_index = (self.write_index + 1) % self.capacity
        self.read_index = (self.read_index + 1) % self.capacity

    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_index = 0
        self.write_index = 0
        self.size = 0
