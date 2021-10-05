from deque1 import Deque, Empty


class PythonListDeque(Deque):
    """A deque implemented using the python list data structure.

    Instantiate a deque object
        >>> a_deque = PythonListDeque()

    Add an item to the end of the deque
        >>> a_deque.enqueue_last(1, 100)

    Add an item to the front of the deque
        >>> a_deque.enqueue_first(2, 200)

    Get the first element of the deque without removing it from the deque
        >>> a_deque.get_first()
        (2, 200)

    Get the last element of the deque without removing it from the deque
        >>> a_deque.get_last()
        (1, 100)

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
        (2, 200)

    Get and remove the last element of the deque
        >>> a_deque.dequeue_last()
        (1, 100)
    """

    def __init__(self):
        self.__key_store = []
        self.__value_store = []

    def __len__(self):
        return len(self.__key_store)

    def is_empty(self):
        return len(self.__key_store) == 0

    def enqueue_first(self, key, value):
        self.__key_store.insert(0, key)
        self.__value_store.insert(0, value)

    def enqueue_last(self, key, value):
        self.__key_store.append(key)
        self.__value_store.append(value)

    def dequeue_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__key_store.pop(0), self.__value_store.pop(0)

    def dequeue_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__key_store.pop(), self.__value_store.pop()

    def get_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__key_store[0], self.__value_store[0]

    def get_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__key_store[-1], self.__value_store[-1]
