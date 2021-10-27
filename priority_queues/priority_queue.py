from abc import ABC, abstractmethod
from typing import Any, Union


class Empty(Exception):
    pass


class PriorityQueue(ABC):
    """A priority queue is a queue ADT that supports insertion (enqueueing) of elements at one end and removal
    (dequeueing) of elements from the opposite end, with the extra attribute of priority of each element it contains,
    meaning an element can move closer to the front of the queue if the elements in front of it are of less precedence
    than itself.
    """

    def __init__(self, minimum_priority_queue: bool):
        self._minimum_priority_queue = minimum_priority_queue

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
    def enqueue(self, x: Any, priority: Union[int, float]) -> None:
        """Insert an element to the end of the queue

        :param x: element to add to the queue
        :param priority: value that determines precedence of x in relation to the rest of the elements in the queue
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
