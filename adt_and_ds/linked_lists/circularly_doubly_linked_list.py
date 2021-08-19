from typing import Union


class Empty(Exception):
    pass


class _BaseNode:
    def __init__(self, previous_node, next_node):
        self.previous_node = previous_node
        self.next_node = next_node


class _Node(_BaseNode):
    def __init__(self, data, previous_node: Union[_BaseNode, None] = None, next_node: Union[_BaseNode, None] = None):
        super().__init__(previous_node, next_node)
        self.data = data


class _SentinelNode(_BaseNode):
    def __init__(self, previous_node: Union[_BaseNode, None] = None, next_node: Union[_BaseNode, None] = None):
        super().__init__(previous_node, next_node)


class CircularlyDoublyLinkedList:
    def __init__(self):
        self.__head = _SentinelNode()
        self.__tail = _SentinelNode(previous_node=self.__head, next_node=self.__head)
        self.__length = 0
        self.__current_node: Union[_Node, None] = None

        self.__head.next_node, self.__head.previous_node = self.__tail, self.__tail

    def __len__(self):
        """ Returns total number of items in list. Time complexity: O(1).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> len(l_list)
        0
        >>> l_list.append(1)
        >>> len(l_list)
        1

        :return: total number of items in list
        """
        return self.__length

    def __repr__(self):
        """ Returns a string representation of the list. Time complexity: O(n).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list
        []
        >>> l_list.append(0)
        >>> l_list
        [0]
        >>> l_list.append(1)
        >>> l_list
        [0, 1]

        :return: string representation of the list
        """
        if self.__length == 0:
            return "[]"

        current_node = self.__head.next_node
        s = f"["

        while not isinstance(current_node, _SentinelNode):
            s += f"{current_node.data}, "
            current_node = current_node.next_node

        return f"{s[:-2]}]"

    def __iter__(self):
        """ Returns a circularly doubly linked list iterable. Time complexity: O(1).

        >>> from collections.abc import Iterable
        >>> l_list = CircularlyDoublyLinkedList()
        >>> isinstance(l_list, Iterable)
        True
        >>> l_list.append(0)
        >>> iterable = iter(l_list)
        >>> next(iterable)
        0
        >>> next(iterable)
        Traceback (most recent call last):
        ...
        StopIteration

        :return: singly linked list iterable
        """
        return self

    def __next__(self):
        """ Returns next item of circularly doubly linked list iterator. Time complexity: O(1).

        >>> from collections.abc import Iterator
        >>> l_list = CircularlyDoublyLinkedList()
        >>> isinstance(l_list, Iterator)
        True
        >>> l_list.append(0)
        >>> next(l_list)
        0
        >>> next(l_list)
        Traceback (most recent call last):
        ...
        StopIteration

        :return: next item
        """
        self.__current_node = self.__head if self.__current_node is None else self.__current_node.next_node
        next_node = self.__current_node.next_node

        if isinstance(next_node, _SentinelNode):
            self.__current_node = None
            raise StopIteration

        return next_node.data

    def __getitem__(self, idx: Union[int, slice]):
        """ Returns item at a specific index, or items in a slice range of the list. Time complexity: O(n).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.append(0)
        >>> l_list.append(1)
        >>> l_list.append(2)
        >>> l_list.append(3)
        >>> l_list.append(4)
        >>> l_list.append(5)
        >>> l_list[0]
        0
        >>> l_list[6]
        Traceback (most recent call last):
        ...
        IndexError: Index out of range
        >>> l_list[1:5:2]
        [1, 3]
        >>> l_list[-1:6]
        Traceback (most recent call last):
        ...
        IndexError: Index out of range
        >>> l_list[1:5:0]
        Traceback (most recent call last):
        ...
        ValueError: Step needs to be greater than zero
        >>> l_list[""]
        Traceback (most recent call last):
        ...
        TypeError

        :return: item at a specific index, or items in a slice range
        """
        if isinstance(idx, int):
            if idx < 0 or idx >= self.__length:
                raise IndexError("Index out of range")

            current_node = self.__head.next_node

            for i in range(idx):
                current_node = current_node.next_node

            return current_node.data

        elif isinstance(idx, slice):
            start = 0 if idx.start is None else idx.start
            stop = self.__length if idx.stop is None else idx.stop
            step = 1 if idx.step is None else idx.step

            if step <= 0:
                raise ValueError("Step needs to be greater than zero")

            if start < 0 or start > self.__length or stop < 0 or stop > self.__length:
                raise IndexError("Index out of range")

            a_list = CircularlyDoublyLinkedList()
            current_node = self.__head.next_node
            i = 0
            skipped = 0

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
        """ Replaces item at a specific index. Time complexity: O(n).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.append(0)
        >>> l_list[0]
        0
        >>> l_list[0] = 1
        >>> l_list[0]
        1
        >>> l_list[1] = 1
        Traceback (most recent call last):
        ...
        IndexError: Index out of range
        """
        if idx < 0 or idx >= self.__length:
            raise IndexError("Index out of range")

        current_node = self.__head.next_node

        for i in range(idx):
            current_node = current_node.next_node

        current_node.data = data

    def __delitem__(self, idx: int):
        """ Deletes item at a specific index. Time complexity: O(n).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.append(0)
        >>> len(l_list)
        1
        >>> del l_list[0]
        >>> len(l_list)
        0
        >>> del l_list[1]
        Traceback (most recent call last):
        ...
        IndexError: Index out of range
        """
        if idx < 0 or idx >= self.__length:
            raise IndexError("Index out of range")

        self.__length -= 1
        previous_node = self.__head
        current_node = previous_node.next_node

        for i in range(idx):
            previous_node = current_node
            current_node = current_node.next_node

        CircularlyDoublyLinkedList._remove_between(previous_node, current_node.next_node)

    @staticmethod
    def _insert_between(new_node: _BaseNode, node1: _BaseNode, node2: _BaseNode):
        """ Helper function that adds a node between two other nodes. Time complexity: O(1).

        >>> node_1, node_2 = _Node(0), _Node(1)
        >>> node_1.next_node, node_2.previous_node = node_2, node_1
        >>> isinstance(node_1.next_node.next_node, _Node)
        False
        >>> CircularlyDoublyLinkedList._insert_between(_Node(2), node_1, node_2)
        >>> isinstance(node_1.next_node.next_node, _Node)
        True
        """
        node1.next_node, new_node.next_node = new_node, node2
        new_node.previous_node, node2.previous_node = node1, new_node

    @staticmethod
    def _remove_between(node1: _BaseNode, node2: _BaseNode):
        """ Helper function that removes a node between two other nodes. Time complexity: O(1).

        >>> node_1, node_2, node_3 = _Node(0), _Node(1), _Node(2)
        >>> node_1.next_node, node_2.next_node = node_2, node_3
        >>> node_2.previous_node, node_3.previous_node = node_1, node_2
        >>> isinstance(node_1.next_node.next_node, _Node)
        True
        >>> CircularlyDoublyLinkedList._remove_between(node_1, node_3)
        >>> isinstance(node_1.next_node.next_node, _Node)
        False
        """
        node1.next_node, node2.previous_node = node2, node1

    def insert(self, idx: int, data):
        """ Add item at a specific index of the list. Time complexity: O(n).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.insert(0, 3)
        Traceback (most recent call last):
        ...
        IndexError: Index out of range
        >>> l_list.append(0)
        >>> l_list.append(1)
        >>> l_list.insert(1, 3)
        >>> l_list
        [0, 3, 1]
        >>> l_list.insert(5, 3)
        Traceback (most recent call last):
        ...
        IndexError: Index out of range
        """
        if idx < 0 or idx >= self.__length:
            raise IndexError("Index out of range")

        self.__length += 1
        previous_node = self.__head
        current_node = previous_node.next_node

        for i in range(idx):
            previous_node = current_node
            current_node = current_node.next_node

        CircularlyDoublyLinkedList._insert_between(_Node(data), previous_node, current_node)

    def insert_first(self, data):
        """ Add item at the head of the list. Time complexity: O(1).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.insert_first(0)
        >>> l_list.insert_first(1)
        >>> l_list
        [1, 0]
        """
        self.__length += 1
        CircularlyDoublyLinkedList._insert_between(_Node(data), self.__head, self.__head.next_node)

    def insert_last(self, data):
        """ Add item at the tail of the list. Time complexity: O(1).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.insert_last(0)
        >>> l_list.insert_last(1)
        >>> l_list
        [0, 1]
        """
        self.__length += 1
        CircularlyDoublyLinkedList._insert_between(_Node(data), self.__tail.previous_node, self.__tail)

    def append(self, data):
        """ Alias of insert_last

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.append(0)
        >>> l_list.append(1)
        >>> l_list
        [0, 1]
        """
        self.insert_last(data)

    def remove_first(self):
        """ Delete item at the head of the list. Time complexity: O(1).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.remove_first()
        Traceback (most recent call last):
        ...
        circularly_doubly_linked_list.Empty: List is empty
        >>> l_list.append(0)
        >>> l_list.append(1)
        >>> l_list.remove_first()
        >>> l_list
        [1]
        """
        if self.__length == 0:
            raise Empty("List is empty")

        self.__length -= 1
        current_node = self.__head.next_node

        CircularlyDoublyLinkedList._remove_between(self.__head, current_node.next_node)

    def remove_last(self):
        """ Delete item at the tail of the list. Time complexity: O(1).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.remove_last()
        Traceback (most recent call last):
        ...
        circularly_doubly_linked_list.Empty: List is empty
        >>> l_list.append(0)
        >>> l_list.append(1)
        >>> l_list.remove_last()
        >>> l_list
        [0]
        """
        if self.__length == 0:
            raise Empty("List is empty")

        self.__length -= 1
        current_node = self.__tail.previous_node
        previous_node = current_node.previous_node

        CircularlyDoublyLinkedList._remove_between(previous_node, self.__tail)

    def get_first(self):
        """ Returns item at the head of the list. Time complexity: O(1).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.get_first()
        Traceback (most recent call last):
        ...
        circularly_doubly_linked_list.Empty: List is empty
        >>> l_list.append(0)
        >>> l_list.append(1)
        >>> l_list.get_first()
        0
        """
        if self.__length == 0:
            raise Empty("List is empty")

        return self.__head.next_node.data

    def get_last(self):
        """ Returns item at the tail of the list. Time complexity: O(1).

        >>> l_list = CircularlyDoublyLinkedList()
        >>> l_list.get_last()
        Traceback (most recent call last):
        ...
        circularly_doubly_linked_list.Empty: List is empty
        >>> l_list.append(0)
        >>> l_list.append(1)
        >>> l_list.get_last()
        1
        """
        if self.__length == 0:
            raise Empty("List is empty")

        return self.__tail.previous_node.data
