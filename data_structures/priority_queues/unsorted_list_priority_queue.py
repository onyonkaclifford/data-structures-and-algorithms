from typing import Any, Union

from priority_queue import Empty, PriorityQueue


class UnsortedListPriorityQueue(PriorityQueue):
    """
    An unsorted list priority queue is a priority queue implemented using python's list data structure that contains
    unsorted items
    """

    def __init__(self, minimum_priority_queue: bool = True):
        super().__init__(minimum_priority_queue)
        self.__data_store = []
        self.__priority_store = []

    def __len__(self) -> int:
        """Get the total number of elements stored in the queue

            >>> a_queue = UnsortedListPriorityQueue()
            >>> a_queue.enqueue(1, 2)
            >>> len(a_queue)
            1

        :returns: count of elements in queue
        """
        return len(self.__data_store)

    def is_empty(self) -> bool:
        """Check if queue contains no elements

            >>> a_queue = UnsortedListPriorityQueue()
            >>> a_queue.is_empty()
            True
            >>> a_queue.enqueue(1, 2)
            >>> a_queue.is_empty()
            False

        :return: True if queue is empty, else False
        """
        return len(self.__data_store) == 0

    def enqueue(self, x: Any, priority: Union[int, float]) -> None:
        """Insert an element to the end of the queue

            >>> a_queue = UnsortedListPriorityQueue()
            >>> a_queue.enqueue(1, 2)

        :param x: element to add to the queue
        :param priority: value that determines precedence of x in relation to the rest of the elements in the queue
        """
        self.__data_store.append(x)
        self.__priority_store.append(priority)

    def dequeue(self) -> Any:
        """Remove first element of the queue and return it

            >>> a_queue = UnsortedListPriorityQueue()
            >>> a_queue.enqueue(1, 2)
            >>> a_queue.dequeue()
            (1, 2)

        :return: first element of queue
        """
        if self.is_empty():
            raise Empty("Queue is empty")

        current_idx = 0
        current_priority = self.__priority_store[0]

        if self._minimum_priority_queue:
            for i, priority in enumerate(self.__priority_store):
                if priority < current_priority:
                    current_idx = i
                    current_priority = priority

        else:
            for i, priority in enumerate(self.__priority_store):
                if priority > current_priority:
                    current_idx = i
                    current_priority = priority

        return self.__data_store.pop(current_idx), self.__priority_store.pop(
            current_idx
        )

    def get_first(self) -> Any:
        """Return first element of the queue without removing it

            >>> a_queue = UnsortedListPriorityQueue()
            >>> a_queue.enqueue(1, 2)
            >>> a_queue.get_first()
            (1, 2)

        :return: first element of queue
        """
        if self.is_empty():
            raise Empty("Queue is empty")

        current_priority = self.__priority_store[0]
        current_element_value = self.__data_store[0]

        if self._minimum_priority_queue:
            for i, priority in enumerate(self.__priority_store):
                if priority < current_priority:
                    current_priority = priority
                    current_element_value = self.__data_store[i]

        else:
            for i, priority in enumerate(self.__priority_store):
                if priority > current_priority:
                    current_priority = priority
                    current_element_value = self.__data_store[i]

        return current_element_value, current_priority
