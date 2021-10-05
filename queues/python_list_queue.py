from queue1 import Empty, Queue


class PythonListQueue(Queue):
    """A queue implemented using the python list data structure.

    Instantiate a queue object
        >>> a_queue = PythonListQueue()

    Add an item to the end of the queue
        >>> a_queue.enqueue(1, 100)

    Get the first element of the queue without removing it from the queue
        >>> a_queue.get_first()
        (1, 100)

    Check if a queue is empty
        >>> a_queue.is_empty()
        False
        >>> PythonListQueue().is_empty()
        True

    Get the length of the queue
        >>> len(a_queue)
        1
        >>> len(PythonListQueue())
        0

    Get and remove the first element of the queue
        >>> a_queue.dequeue()
        (1, 100)
    """

    def __init__(self):
        self.__key_store = []
        self.__value_store = []

    def __len__(self):
        return len(self.__key_store)

    def is_empty(self):
        return len(self.__key_store) == 0

    def enqueue(self, key, value):
        self.__key_store.append(key)
        self.__value_store.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__key_store.pop(0), self.__value_store.pop(0)

    def get_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__key_store[0], self.__value_store[0]
