from priority_queue import PriorityQueue
from queue1 import Empty


class UnsortedListPriorityQueue(PriorityQueue):
    """An unsorted list priority queue is a priority queue implemented using a python list data structure that contains
    unsorted items.

    Instantiate a queue object
        >>> a_queue = UnsortedListPriorityQueue(minimum=True)

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
        >>> UnsortedListPriorityQueue(minimum=True).is_empty()
        True

    Get the length of the queue
        >>> len(a_queue)
        3
        >>> len(UnsortedListPriorityQueue(minimum=True))
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
        self.__key_store.append(key)
        self.__value_store.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        current_idx = 0
        current_key = self.__key_store[0]

        if self._minimum:
            for i, key in enumerate(self.__key_store):
                if key < current_key:
                    current_idx = i
                    current_key = key

        else:
            for i, key in enumerate(self.__key_store):
                if key > current_key:
                    current_idx = i
                    current_key = key

        return self.__key_store.pop(current_idx), self.__value_store.pop(current_idx)

    def get_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        current_key = self.__key_store[0]
        current_value = self.__value_store[0]

        if self._minimum:
            for i, key in enumerate(self.__key_store):
                if key < current_key:
                    current_key = key
                    current_value = self.__value_store[i]

        else:
            for i, key in enumerate(self.__key_store):
                if key > current_key:
                    current_key = key
                    current_value = self.__value_store[i]

        return current_key, current_value
