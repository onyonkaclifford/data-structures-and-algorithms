from abc import ABC, abstractmethod
from typing import Any


class Empty(Exception):
    pass


class Queue(ABC):
    """A queue is a First-In-First-Out ADT that supports insertion (enqueueing) of elements at one end and removal
    (dequeueing) of elements from the opposite end. The order in which elements are enqueued is maintained when
    dequeueing them.
    """

    @abstractmethod
    def __len__(self) -> int:
        """Get the total number of elements stored in the queue

        :returns: count of elements in queue
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if queue contains no elements

        :return: True if queue is empty, else False
        """
        pass

    @abstractmethod
    def enqueue(self, x: Any) -> None:
        """Insert an element to the end of the queue

        :param x: element to add to the queue
        """
        pass

    @abstractmethod
    def dequeue(self) -> Any:
        """Remove first element of the queue and return it

        :return: first element of queue
        """
        pass

    @abstractmethod
    def get_first(self) -> Any:
        """Return first element of the queue without removing it

        :return: first element of queue
        """
        pass
