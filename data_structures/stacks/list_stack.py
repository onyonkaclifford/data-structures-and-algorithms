from typing import Any

from stack import Empty, Stack


class ListStack(Stack):
    """
    A stack implemented using python's list data structure
    """

    def __init__(self):
        self.__data_store = []

    def __len__(self) -> int:
        """Get the total number of elements stored in the stack

            >>> a_stack = ListStack()
            >>> a_stack.push(1)
            >>> len(a_stack)
            1

        :returns: count of elements in stack
        """
        return len(self.__data_store)

    def is_empty(self) -> bool:
        """Check if stack contains no elements

            >>> a_stack = ListStack()
            >>> a_stack.is_empty()
            True
            >>> a_stack.push(1)
            >>> a_stack.is_empty()
            False

        :return: True if stack is empty, else False
        """
        return len(self.__data_store) == 0

    def push(self, x: Any):
        """Insert element x to the top of the stack

            >>> a_stack = ListStack()
            >>> a_stack.push(1)

        :param x: element to add to the stack
        """
        self.__data_store.append(x)

    def pop(self) -> Any:
        """Get element at the top of the stack, and remove it from the stack

            >>> a_stack = ListStack()
            >>> a_stack.push(1)
            >>> a_stack.pop()
            1

        :return: element at top of stack
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.__data_store.pop()

    def peek(self) -> Any:
        """Get element at the top of the stack without removing it

            >>> a_stack = ListStack()
            >>> a_stack.push(1)
            >>> a_stack.peek()
            1

        :return: element at top of stack
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.__data_store[-1]
