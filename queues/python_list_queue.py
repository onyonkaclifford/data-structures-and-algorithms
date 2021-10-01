from queue1 import Empty, Queue


class PythonListQueue(Queue):
    """A queue implemented using the python list data structure.

    Instantiate a queue object
        >>> a_queue = PythonListQueue()

    Add an item to the end of the queue
        >>> a_queue.enqueue(1)

    Get the first element of the queue without removing it from the queue
        >>> a_queue.get_first()
        1

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
        1
    """

    def __init__(self):
        self.__data_store = []

    def __len__(self):
        return len(self.__data_store)

    def is_empty(self):
        return len(self.__data_store) == 0

    def enqueue(self, x):
        self.__data_store.append(x)

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__data_store.pop(0)

    def get_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__data_store[0]
