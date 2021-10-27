from typing import Any

from deque import Deque, Empty


class ListDeque(Deque):
    """
    A deque implemented using python's list data structure
    """

    def __init__(self):
        self.__data_store = []

    def __len__(self) -> int:
        """Get the total number of elements stored in the deque

            >>> a_deque = ListDeque()
            >>> a_deque.enqueue_last(1)
            >>> len(a_deque)
            1

        :returns: count of elements in deque
        """
        return len(self.__data_store)

    def is_empty(self) -> bool:
        """Check if deque contains no elements

            >>> a_deque = ListDeque()
            >>> a_deque.is_empty()
            True
            >>> a_deque.enqueue_last(1)
            >>> a_deque.is_empty()
            False

        :return: True if deque is empty, else False
        """
        return len(self.__data_store) == 0

    def enqueue_first(self, x: Any) -> None:
        """Insert an element to the front of the deque

            >>> a_deque = ListDeque()
            >>> a_deque.enqueue_first(1)

        :param x: element to add to the deque
        """
        self.__data_store.insert(0, x)

    def enqueue_last(self, x: Any) -> None:
        """Insert an element to the end of the deque

            >>> a_deque = ListDeque()
            >>> a_deque.enqueue_last(1)

        :param x: element to add to the deque
        """
        self.__data_store.append(x)

    def dequeue_first(self) -> Any:
        """Remove first element of the deque and return it

            >>> a_deque = ListDeque()
            >>> a_deque.enqueue_last(1)
            >>> a_deque.dequeue_first()
            1

        :return: first element of deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store.pop(0)

    def dequeue_last(self) -> Any:
        """Remove last element of the deque and return it

            >>> a_deque = ListDeque()
            >>> a_deque.enqueue_last(1)
            >>> a_deque.dequeue_last()
            1

        :return: last element of deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store.pop()

    def get_first(self) -> Any:
        """Return first element of the deque without removing it

            >>> a_deque = ListDeque()
            >>> a_deque.enqueue_last(1)
            >>> a_deque.get_first()
            1

        :return: first element of deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store[0]

    def get_last(self) -> Any:
        """Return last element of the deque without removing it

            >>> a_deque = ListDeque()
            >>> a_deque.enqueue_last(1)
            >>> a_deque.get_last()
            1

        :return: last element of deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data_store[-1]
