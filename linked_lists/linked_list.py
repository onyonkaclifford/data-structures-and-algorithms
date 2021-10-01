import copy
from abc import ABC, abstractmethod
from typing import Union


class Empty(Exception):
    pass


class _BaseNode(ABC):
    def __init__(self, previous_node, next_node):
        self.previous_node = previous_node
        self.next_node = next_node


class LinkedList(ABC):
    """A linked list is a collection of nodes, with each node containing a reference to the node preceding it, or the
    node succeeding it, or both. Data structures that implement this abstract data type include:

    1. singly linked list
    2. circularly singly linked list
    3. doubly linked list
    4. circularly doubly linked list

    For each of these data structures, the implementation details may defer between one implementation and another. One
    implementation may use sentinel nodes to denote the head and tail nodes, whereas another may use normal nodes with
    references to items within the list for the head and tail. The implementation details may also change depending
    on the context that these data structures will be used in, so as to best optimise them to the tasks within that
    specific context.

    The implementation of the various linked list data structures defined within this project is meant to provide a
    uniform behaviour for all the data structures, such that one data structure may be replaced with another seamlessly.
    """

    class _Node(_BaseNode):
        def __init__(
            self,
            data,
            previous_node: Union[_BaseNode, None] = None,
            next_node: Union[_BaseNode, None] = None,
        ):
            super().__init__(previous_node, next_node)
            self.data = data

    class _SentinelNode(_BaseNode):
        def __init__(
            self,
            previous_node: Union[_BaseNode, None] = None,
            next_node: Union[_BaseNode, None] = None,
        ):
            super().__init__(previous_node, next_node)

    def __init__(self):
        self._head = LinkedList._SentinelNode()
        self._tail = LinkedList._SentinelNode()
        self._length = 0
        self.__current_node: Union[LinkedList._Node, None] = None

    def __len__(self):
        """Returns total number of items in list. Time complexity: O(1).

        :return: total number of items in list
        """
        return self._length

    def __repr__(self):
        """Returns a string representation of the list. Time complexity: O(n).

        :return: string representation of the list
        """
        if self._length == 0:
            return "[]"

        current_node = self._head.next_node
        s = "["

        while not isinstance(current_node, LinkedList._SentinelNode):
            s += f"{current_node.data}, "
            current_node = current_node.next_node

        return f"{s[:-2]}]"

    def __iter__(self):
        """Returns a linked list iterable. Time complexity: O(1).

        :return: linked list iterable
        """
        return self

    def __next__(self):
        """Returns next item of linked list iterator. Time complexity: O(1).

        :return: next item
        :raises StopIteration: when the cursor denoting the current item surpasses the last item of the list
        """
        self.__current_node = (
            self._head if self.__current_node is None else self.__current_node.next_node
        )
        next_node = self.__current_node.next_node

        if isinstance(next_node, LinkedList._SentinelNode):
            self.__current_node = None
            raise StopIteration

        return next_node.data

    def __getitem__(self, idx: Union[int, slice]):
        """Returns item at a specific index, or items in a slice range of the list. Time complexity: O(n).

        :param idx: index or slice range of items within the list
        :return: item at a specific index, or items in a slice range
        :raises IndexError: when the index or slice passed is out of range
        :raises ValueError: when the step of the slice passed less than one
        """
        if isinstance(idx, int):
            if idx < 0 or idx >= self._length:
                raise IndexError("Index out of range")

            current_node = self._head.next_node

            for i in range(idx):
                current_node = current_node.next_node

            return current_node.data

        elif isinstance(idx, slice):
            start = 0 if idx.start is None else idx.start
            stop = self._length if idx.stop is None else idx.stop
            step = 1 if idx.step is None else idx.step

            if step <= 0:
                raise ValueError("Step needs to be greater than zero")

            if start < 0 or start > self._length or stop < 0 or stop > self._length:
                raise IndexError("Index out of range")

            current_node = self._head.next_node
            a_list = copy.deepcopy(self)
            i = 0
            skipped = 0

            a_list.remove_all()

            while i < stop:
                if i == start or (i >= start and skipped == step):
                    a_list.append(current_node.data)
                    skipped = 0

                current_node = current_node.next_node
                i += 1
                skipped += 1

            return a_list

        else:
            raise TypeError

    def __setitem__(self, idx: int, data):
        """Replaces item at a specific index. Time complexity: O(n).

        :param idx: index of item to be replaced
        :param data: new item to replace existing item
        :raises IndexError: when the index passed is out of range
        """
        if idx < 0 or idx >= self._length:
            raise IndexError("Index out of range")

        current_node = self._head.next_node

        for i in range(idx):
            current_node = current_node.next_node

        current_node.data = data

    def __delitem__(self, idx: int):
        """Deletes item at a specific index. Time complexity: O(n).

        :param idx: index of item to be deleted
        :raises IndexError: when the index passed is out of range
        """
        if idx < 0 or idx >= self._length:
            raise IndexError("Index out of range")

        self._length -= 1
        previous_node = self._head
        current_node = previous_node.next_node

        for i in range(idx):
            previous_node = current_node
            current_node = current_node.next_node

        self._remove_between(previous_node, current_node.next_node)

    @staticmethod
    @abstractmethod
    def _insert_between(new_node: _BaseNode, node1: _BaseNode, node2: _BaseNode):
        """Helper function that inserts a node between two other nodes

        :param new_node: node to be inserted
        :param node1: node at the start
        :param node2: node at the end
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def _remove_between(node1: _BaseNode, node2: _BaseNode):
        """Helper function that removes a node between two other nodes

        :param node1: node at the start
        :param node2: node at the end
        """
        raise NotImplementedError

    def insert(self, idx: int, data):
        """Add item at a specific index of the list. Time complexity: O(n).

        :param idx: index to insert item at
        :param data: item to insert
        :raises IndexError: when the index passed is out of range
        """
        if idx < 0 or idx >= self._length:
            raise IndexError("Index out of range")

        self._length += 1
        previous_node = self._head
        current_node = previous_node.next_node

        for i in range(idx):
            previous_node = current_node
            current_node = current_node.next_node

        self._insert_between(LinkedList._Node(data), previous_node, current_node)

    def insert_first(self, data):
        """Add item at the head of the list. Time complexity: O(1).

        :param data: item to insert
        """
        self._length += 1
        self._insert_between(LinkedList._Node(data), self._head, self._head.next_node)

    @abstractmethod
    def insert_last(self, data):
        """Add item at the tail of the list

        :param data: item to insert
        """
        raise NotImplementedError

    def append(self, data):
        """Alias of insert_last

        :param data: item to insert
        """
        self.insert_last(data)

    def remove_all(self):
        """Delete all items from the list. Time complexity: O(1)."""
        self.__init__()

    def remove_first(self):
        """Delete item at the head of the list. Time complexity: O(1).

        :raises Empty: when the list is empty
        """
        if self._length == 0:
            raise Empty("List is empty")

        self._length -= 1
        current_node = self._head.next_node

        self._remove_between(self._head, current_node.next_node)

    @abstractmethod
    def remove_last(self):
        """Delete item at the tail of the list"""
        raise NotImplementedError

    def get_first(self):
        """Returns item at the head of the list. Time complexity: O(1).

        :return: first item in list
        :raises Empty: when the list is empty
        """
        if self._length == 0:
            raise Empty("List is empty")

        return self._head.next_node.data

    @abstractmethod
    def get_last(self):
        """Returns item at the tail of the list

        :return: last item in list
        """
        raise NotImplementedError
