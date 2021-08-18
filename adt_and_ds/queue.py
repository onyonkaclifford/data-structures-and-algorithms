class Empty(Exception):
    pass


class Queue:
    """ A queue is a First-In-First-Out structure that supports insertion (queueing) of elements at one end and removal
    (dequeueing) of elements from the opposite end. The order in which elements are enqueued is maintained when
    dequeued them.
    """
    def __init__(self):
        self.__data_store = []

    def __len__(self):
        return len(self.__data_store)

    def is_empty(self):
        """ Check if queue contains no elements. Time complexity: O(1).

        >>> queue = Queue()
        >>> queue.is_empty()
        True
        >>> queue.enqueue(1)
        >>> queue.is_empty()
        False

        :return: True if queue is empty, else False
        """
        return len(self.__data_store) == 0

    def enqueue(self, x):
        """ Insert element x to the end of the queue. Time complexity: O(1).

        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> len(queue)
        1

        :param x: element to add to the queue
        """
        self.__data_store.append(x)

    def dequeue(self):
        """ Remove first element of the queue and return it. Time complexity: O(1).

        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.dequeue()
        1
        >>> queue.dequeue()
        Traceback (most recent call last):
        ...
        queue.Empty: Queue is empty

        :return: first element of queue
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__data_store.pop(0)

    def first(self):
        """ Return first element of the queue without removing it. Time complexity: O(1).

        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.first()
        1
        >>> queue.dequeue()
        1
        >>> queue.first()
        Traceback (most recent call last):
        ...
        queue.Empty: Queue is empty

        :return: first element of queue
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__data_store[0]
