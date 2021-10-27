from abc import ABC, abstractmethod
from typing import Any


class Empty(Exception):
    pass


class Stack(ABC):
    """A stack is a Last-In-First-Out ADT that supports insertion (pushing) and removal (popping) of elements
    from the same end. The order in which elements are pushed into the stack is reversed when popping out elements from
    the stack.
    """

    @abstractmethod
    def __len__(self) -> int:
        """Get the total number of elements stored in the stack

        :returns: count of elements in stack
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if stack contains no elements

        :return: True if stack is empty, else False
        """
        pass

    @abstractmethod
    def push(self, x: Any) -> None:
        """Insert element x to the top of the stack

        :param x: element to add to the stack
        """
        pass

    @abstractmethod
    def pop(self) -> Any:
        """Get element at the top of the stack, and remove it from the stack

        :return: element at top of stack
        """
        pass

    @abstractmethod
    def peek(self) -> Any:
        """Get element at the top of the stack without removing it

        :return: element at top of stack
        """
        pass
