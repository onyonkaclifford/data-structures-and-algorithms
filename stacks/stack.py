from abc import ABC, abstractmethod


class Empty(Exception):
    pass


class Stack(ABC):
    """A stack is a Last-In-First-Out structure that supports insertion (pushing) and removal (popping) of elements
    from the same end. The order in which elements are pushed into the stack is reversed when popping out elements from
    the stack.
    """

    @abstractmethod
    def __len__(self):
        """Returns the total number of elements stored in the stack

        :returns: the total number of elements stored in the stack
        """
        raise NotImplementedError

    @abstractmethod
    def is_empty(self):
        """Check if stack contains no elements

        :return: True if stack is empty, else False
        """
        raise NotImplementedError

    @abstractmethod
    def push(self, x):
        """Insert element x to the top of the stack

        :param x: element to add to the stack
        """
        raise NotImplementedError

    @abstractmethod
    def pop(self):
        """Remove an element from the top of the stack and return it

        :return: element at top of stack
        """
        raise NotImplementedError

    @abstractmethod
    def peek(self):
        """Return element at the top of the stack without removing it

        :return: element at top of stack
        """
        raise NotImplementedError
