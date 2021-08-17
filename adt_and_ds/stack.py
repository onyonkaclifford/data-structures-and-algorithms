class Empty(Exception):
    pass


class Stack:
    """ A stack is a Last-In-First-Out structure that supports insertion (pushing) and removal (popping) of elements
    from the same end. The order in which elements are pushed into the stack is reversed when popping out elements from
    the stack.
    """
    def __init__(self):
        self.__data_store = []

    def __len__(self):
        return len(self.__data_store)

    def is_empty(self):
        """ Check if stack contains no elements

        >>> stack = Stack()
        >>> stack.is_empty()
        True
        >>> stack.push(1)
        >>> stack.is_empty()
        False

        :return: bool
        """
        return len(self.__data_store) == 0

    def push(self, x):
        """ Insert element x to the top of the stack

        >>> stack = Stack()
        >>> stack.push(1)
        >>> len(stack)
        1

        :param x: element to add to the stack
        """
        self.__data_store.append(x)

    def pop(self):
        """ Remove an element from the top of the stack and return it

        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.pop()
        1
        >>> stack.pop()
        Traceback (most recent call last):
        ...
        stack.Empty: Stack is empty

        :return: element at top of stack
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.__data_store.pop()

    def peek(self):
        """ Return element at the top of the stack without removing it

        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.peek()
        1
        >>> stack.pop()
        1
        >>> stack.peek()
        Traceback (most recent call last):
        ...
        stack.Empty: Stack is empty

        :return: element at top of stack
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.__data_store[-1]
