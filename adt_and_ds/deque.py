class Empty(Exception):
    pass


class Deque:
    """ A deque is a structure that supports insertion and removal of elements from either end. It's also referred to
    as a double-ended queue.
    """
    def __init__(self):
        self.__data_store = []

    def __len__(self):
        return len(self.__data_store)

    def is_empty(self):
        """ Check if deque contains no elements. Time complexity: O(1).

        >>> deque = Deque()
        >>> deque.is_empty()
        True
        >>> deque.enqueue_first(1)
        >>> deque.is_empty()
        False

        :return: True if deque is empty, else False
        """
        return len(self.__data_store) == 0

    def enqueue_first(self, x):
        """ Insert element x to the front of the deque. Time complexity: O(1).

        >>> deque = Deque()
        >>> deque.enqueue_first(1)
        >>> len(deque)
        1

        :param x: element to add to the deque
        """
        self.__data_store.insert(0, x)

    def enqueue_last(self, x):
        """ Insert element x to the end of the deque. Time complexity: O(1).

        >>> deque = Deque()
        >>> deque.enqueue_last(1)
        >>> len(deque)
        1

        :param x: element to add to the deque
        """
        self.__data_store.append(x)

    def dequeue_first(self):
        """ Remove first element of the deque and return it. Time complexity: O(1).

        >>> deque = Deque()
        >>> deque.enqueue_first(1)
        >>> deque.dequeue_first()
        1
        >>> deque.dequeue_first()
        Traceback (most recent call last):
        ...
        deque.Empty: Deque is empty

        :return: first element of deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store.pop(0)

    def dequeue_last(self):
        """ Remove last element of the deque and return it. Time complexity: O(1).

        >>> deque = Deque()
        >>> deque.enqueue_first(1)
        >>> deque.dequeue_last()
        1
        >>> deque.dequeue_last()
        Traceback (most recent call last):
        ...
        deque.Empty: Deque is empty

        :return: last element of deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store.pop()

    def first(self):
        """ Return first element of the deque without removing it. Time complexity: O(1).

        >>> deque = Deque()
        >>> deque.enqueue_first(1)
        >>> deque.first()
        1
        >>> deque.dequeue_first()
        1
        >>> deque.first()
        Traceback (most recent call last):
        ...
        deque.Empty: Deque is empty

        :return: first element of deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store[0]

    def last(self):
        """ Return last element of the deque without removing it. Time complexity: O(1).

        >>> deque = Deque()
        >>> deque.enqueue_first(1)
        >>> deque.last()
        1
        >>> deque.dequeue_first()
        1
        >>> deque.last()
        Traceback (most recent call last):
        ...
        deque.Empty: Deque is empty

        :return: last element of deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store[-1]
