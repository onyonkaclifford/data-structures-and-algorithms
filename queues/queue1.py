from abc import ABC, abstractmethod


class Empty(Exception):
    pass


class Queue(ABC):
    """A queue is a First-In-First-Out structure that supports insertion (queueing) of elements at one end and removal
    (dequeueing) of elements from the opposite end. The order in which elements are enqueued is maintained when
    dequeued them.
    """

    @abstractmethod
    def __len__(self):
        """Returns the total number of elements stored in the queue

        :returns: the total number of elements stored in the queue
        """
        raise NotImplementedError

    @abstractmethod
    def is_empty(self):
        """Check if queue contains no elements

        :return: True if queue is empty, else False
        """
        raise NotImplementedError

    @abstractmethod
    def enqueue(self, key, value):
        """Insert an element to the end of the queue

        :param key: unique identifier of the element to add to the queue
        :param value: element to add to the queue
        """
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        """Remove first element of the queue and return it

        :return: first element of queue
        """
        raise NotImplementedError

    @abstractmethod
    def get_first(self):
        """Return first element of the queue without removing it

        :return: first element of queue
        """
        raise NotImplementedError
