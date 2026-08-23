class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        super(BufferError, self).__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        super(BufferError, self).__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    @property
    def _buffer_filled(self):
        return [item for item in self.buffer if item != ""]

    def read(self):
        if len(self._buffer_filled) == 0:
            raise BufferEmptyException("Circular buffer is empty")

        return self.buffer.pop(0)

    def write(self, data):

        if len(self._buffer_filled) == self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer.append(data)

    def overwrite(self, data):

        if len(self._buffer_filled) == self.capacity:
            self.buffer.pop(0)

        self.buffer.append(data)

    def clear(self):
        self.buffer = []
