from stack import Stack, Empty


class PythonListStack(Stack):
    """ A stack implemented using the python list data structure.

    Instantiate a stack object
        >>> a_stack = PythonListStack()

    Push an item into the stack
        >>> a_stack.push(1)

    Get the top element of the stack without deleting it
        >>> a_stack.peek()
        1

    Check if the stack is empty
        >>> a_stack.is_empty()
        False
        >>> PythonListStack().is_empty()
        True

    Get the length of the stack
        >>> len(a_stack)
        1
        >>> len(PythonListStack())
        0

    Get and remove element at the top of the stack
        >>> a_stack.pop()
        1
    """
    def __init__(self):
        self.__data_store = []

    def __len__(self):
        return len(self.__data_store)

    def is_empty(self):
        return len(self.__data_store) == 0

    def push(self, x):
        self.__data_store.append(x)

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.__data_store.pop()

    def peek(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.__data_store[-1]
