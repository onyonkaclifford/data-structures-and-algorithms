from abc import ABC, abstractmethod
from typing import Any


class Empty(Exception):
    pass


class Deque(ABC):
    """A deque is an ADT that supports insertion and removal of elements from either end. It's also referred to
    as a double-ended queue.
    """

    @abstractmethod
    def __len__(self) -> int:
        """Get the total number of elements stored in the deque

        :returns: count of elements in deque
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if deque contains no elements

        :return: True if deque is empty, else False
        """
        pass

    @abstractmethod
    def enqueue_first(self, x: Any) -> None:
        """Insert an element to the front of the deque

        :param x: element to add to the deque
        """
        pass

    @abstractmethod
    def enqueue_last(self, x: Any) -> None:
        """Insert an element to the end of the deque

        :param x: element to add to the deque
        """
        pass

    @abstractmethod
    def dequeue_first(self) -> Any:
        """Remove first element of the deque and return it

        :return: first element of deque
        """
        pass

    @abstractmethod
    def dequeue_last(self) -> Any:
        """Remove last element of the deque and return it

        :return: last element of deque
        """
        pass

    @abstractmethod
    def get_first(self) -> Any:
        """Return first element of the deque without removing it

        :return: first element of deque
        """
        pass

    @abstractmethod
    def get_last(self) -> Any:
        """Return last element of the deque without removing it

        :return: last element of deque
        """
        pass
