from typing import Any

from queue_custom import Empty, Queue


class ListQueue(Queue):
    """
    A queue implemented using python's list data structure
    """

    def __init__(self):
        self.__data_store = []

    def __len__(self) -> int:
        """Get the total number of elements stored in the queue

            >>> a_queue = ListQueue()
            >>> a_queue.enqueue(1)
            >>> len(a_queue)
            1

        :returns: count of elements in queue
        """
        return len(self.__data_store)

    def is_empty(self) -> bool:
        """Check if queue contains no elements

            >>> a_queue = ListQueue()
            >>> a_queue.is_empty()
            True
            >>> a_queue.enqueue(1)
            >>> a_queue.is_empty()
            False

        :return: True if queue is empty, else False
        """
        return len(self.__data_store) == 0

    def enqueue(self, x: Any) -> None:
        """Insert an element to the end of the queue

            >>> a_queue = ListQueue()
            >>> a_queue.enqueue(1)

        :param x: element to add to the queue
        """
        self.__data_store.append(x)

    def dequeue(self) -> Any:
        """Remove first element of the queue and return it

            >>> a_queue = ListQueue()
            >>> a_queue.enqueue(1)
            >>> a_queue.dequeue()
            1

        :return: first element of queue
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__data_store.pop(0)

    def get_first(self) -> Any:
        """Return first element of the queue without removing it

            >>> a_queue = ListQueue()
            >>> a_queue.enqueue(1)
            >>> a_queue.get_first()
            1

        :return: first element of queue
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__data_store[0]
