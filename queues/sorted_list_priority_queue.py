from priority_queue import PriorityQueue
from queue1 import Empty


class SortedListPriorityQueue(PriorityQueue):
    """A sorted list priority queue is a priority queue implemented using a python list data structure that contains
    sorted items.

    Instantiate a queue object
        >>> a_queue = SortedListPriorityQueue(minimum=True)

    Add an item to the end of the queue
        >>> a_queue.enqueue(2, 200)
        >>> a_queue.enqueue(3, 300)
        >>> a_queue.enqueue(1, 100)

    Get the first element of the queue without removing it from the queue
        >>> a_queue.get_first()
        (1, 100)

    Check if a queue is empty
        >>> a_queue.is_empty()
        False
        >>> SortedListPriorityQueue(minimum=True).is_empty()
        True

    Get the length of the queue
        >>> len(a_queue)
        3
        >>> len(SortedListPriorityQueue(minimum=True))
        0

    Get and remove the first element of the queue
        >>> a_queue.dequeue()
        (1, 100)
    """

    def __init__(self, minimum: bool):
        super().__init__(minimum)
        self.__key_store = []
        self.__value_store = []

    def __len__(self):
        return len(self.__key_store)

    def is_empty(self):
        return len(self.__key_store) == 0

    def enqueue(self, key, value):
        current_idx = -1

        if self._minimum:
            for i, k in enumerate(self.__key_store):
                if key < k:
                    current_idx = i
                    break

        else:
            for i, k in enumerate(self.__key_store):
                if key > k:
                    current_idx = i
                    break

        if current_idx == -1:
            self.__key_store.append(key)
            self.__value_store.append(value)
        else:
            self.__key_store.insert(current_idx, key)
            self.__value_store.insert(current_idx, value)

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        return self.__key_store.pop(0), self.__value_store.pop(0)

    def get_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        return self.__key_store[0], self.__value_store[0]
