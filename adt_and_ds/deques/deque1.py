from abc import ABC, abstractmethod


class Empty(Exception):
    pass


class Deque(ABC):
    """ A deque is a structure that supports insertion and removal of elements from either end. It's also referred to
    as a double-ended queue.
    """
    @abstractmethod
    def __len__(self):
        raise NotImplementedError

    @abstractmethod
    def is_empty(self):
        """ Check if deque contains no elements

        :return: True if deque is empty, else False
        """
        raise NotImplementedError

    @abstractmethod
    def enqueue_first(self, x):
        """ Insert element x to the front of the deque

        :param x: element to add to the deque
        """
        raise NotImplementedError

    @abstractmethod
    def enqueue_last(self, x):
        """ Insert element x to the end of the deque

        :param x: element to add to the deque
        """
        raise NotImplementedError

    @abstractmethod
    def dequeue_first(self):
        """ Remove first element of the deque and return it

        :return: first element of deque
        """
        raise NotImplementedError

    @abstractmethod
    def dequeue_last(self):
        """ Remove last element of the deque and return it

        :return: last element of deque
        """
        raise NotImplementedError

    @abstractmethod
    def get_first(self):
        """ Return first element of the deque without removing it

        :return: first element of deque
        """
        raise NotImplementedError

    @abstractmethod
    def get_last(self):
        """ Return last element of the deque without removing it

        :return: last element of deque
        """
        raise NotImplementedError
