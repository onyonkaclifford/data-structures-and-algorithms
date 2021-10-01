from deque1 import Deque, Empty


class PythonListDeque(Deque):
    """A deque implemented using the python list data structure.

    Instantiate a deque object
        >>> a_deque = PythonListDeque()

    Add an item to the end of the deque
        >>> a_deque.enqueue_last(1)

    Add an item to the front of the deque
        >>> a_deque.enqueue_first(2)

    Get the first element of the deque without removing it from the deque
        >>> a_deque.get_first()
        2

    Get the last element of the deque without removing it from the deque
        >>> a_deque.get_last()
        1

    Check if a deque is empty
        >>> a_deque.is_empty()
        False
        >>> PythonListDeque().is_empty()
        True

    Get the length of the deque
        >>> len(a_deque)
        2
        >>> len(PythonListDeque())
        0

    Get and remove the first element of the deque
        >>> a_deque.dequeue_first()
        2

    Get and remove the last element of the deque
        >>> a_deque.dequeue_last()
        1
    """

    def __init__(self):
        self.__data_store = []

    def __len__(self):
        return len(self.__data_store)

    def is_empty(self):
        return len(self.__data_store) == 0

    def enqueue_first(self, x):
        self.__data_store.insert(0, x)

    def enqueue_last(self, x):
        self.__data_store.append(x)

    def dequeue_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store.pop(0)

    def dequeue_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store.pop()

    def get_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store[0]

    def get_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store[-1]
