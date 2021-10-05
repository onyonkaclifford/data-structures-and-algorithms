from abc import ABC

from queue1 import Queue


class PriorityQueue(Queue, ABC):
    """A priority queue is a queue structure that supports insertion (queueing) of elements at one end and removal
    (dequeueing) of elements from the opposite end, with the extra calculation of priority that means an element can
    move closer to the front of the queue if the elements in front of it are of less precedence than itself.
    """

    def __init__(self, minimum: bool):
        self._minimum = minimum
