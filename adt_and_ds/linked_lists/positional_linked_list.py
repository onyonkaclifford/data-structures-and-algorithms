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


class _Position:
    """ A representation of the position of a node within a positional linked list """

    def __init__(self, belongs_to, node: _Node):
        self.__variables = {"belongs_to": belongs_to}
        self.__node = node

    def is_owned_by(self, owner):
        """ Check whether position belongs to the list, owner. Time complexity: O(1).

        >>> l_list1, l_list2 = PositionalLinkedList(), PositionalLinkedList()
        >>> _ = l_list1.append(0)
        >>> position1 = l_list1.get_first()
        >>> position1.is_owned_by(l_list1)
        True
        >>> position1.is_owned_by(l_list2)
        False
        """
        return owner is self.__variables["belongs_to"]

    def manipulate_variables(self, owner, method: str, *params):
        """ Manipulate member variables of this position. Methods of the owner list are the only ones that can call
        this method. Time complexity: O(1).

        >>> l_list1, l_list2 = PositionalLinkedList(), PositionalLinkedList()
        >>> _ = l_list1.append(0)
        >>> position1 = l_list1.get_first()
        >>> position1.manipulate_variables(l_list2, "dummy_method", "param1", "param2")
        Traceback (most recent call last):
        ...
        ValueError: Position doesn't belong to the passed owner
        """
        if not self.is_owned_by(owner):
            raise ValueError("Position doesn't belong to the passed owner")
        return getattr(owner, method)(self.__variables, *params)

    def manipulate_node(self, owner, method: str, *params):
        """ Manipulate the node held by this position. Methods of the owner list are the only ones that can call this
        method. Time complexity: O(1).

        >>> l_list1, l_list2 = PositionalLinkedList(), PositionalLinkedList()
        >>> _ = l_list1.append(0)
        >>> position1 = l_list1.get_first()
        >>> position1.manipulate_node(l_list2, "dummy_method", "param1", "param2")
        Traceback (most recent call last):
        ...
        ValueError: Position doesn't belong to the passed owner
        """
        if not self.is_owned_by(owner):
            raise ValueError("Position doesn't belong to the passed owner")
        return getattr(owner, method)(self.__node, *params)

    def get_data(self):
        """ Returns the data stored by the node held by this position. Time complexity: O(1).

        >>> l_list1 = PositionalLinkedList()
        >>> _ = l_list1.append(0)
        >>> position1 = l_list1.get_first()
        >>> position1.get_data()
        0
        """
        return self.__node.data


class PositionalLinkedList:
    def __init__(self):
        self.__head = _SentinelNode()
        self.__tail = _SentinelNode(previous_node=self.__head)
        self.__length = 0
        self.__current_node: Union[_Node, None] = None

        self.__head.next_node = self.__tail

    def __len__(self):
        """ Returns total number of items in list. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> len(l_list)
        0
        >>> _ = l_list.append(1)
        >>> len(l_list)
        1

        :return: total number of items in list
        """
        return self.__length

    def __repr__(self):
        """ Returns a string representation of the list. Time complexity: O(n).

        >>> l_list = PositionalLinkedList()
        >>> l_list
        []
        >>> _ = l_list.append(0)
        >>> l_list
        [0]
        >>> _ = l_list.append(1)
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
        """ Returns a positional linked list iterable. Time complexity: O(1).

        >>> from collections.abc import Iterable
        >>> l_list = PositionalLinkedList()
        >>> isinstance(l_list, Iterable)
        True
        >>> _ = l_list.append(0)
        >>> iterable = iter(l_list)
        >>> next(iterable).get_data()
        0
        >>> next(iterable).get_data()
        Traceback (most recent call last):
        ...
        StopIteration

        :return: singly linked list iterable
        """
        return self

    def __next__(self):
        """ Returns next item of positional linked list iterator. Time complexity: O(1).

        >>> from collections.abc import Iterator
        >>> l_list = PositionalLinkedList()
        >>> isinstance(l_list, Iterator)
        True
        >>> _ = l_list.append(0)
        >>> next(l_list).get_data()
        0
        >>> next(l_list).get_data()
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

        return _Position(self, next_node)

    @staticmethod
    def _insert_between(new_node: _BaseNode, node1: _BaseNode, node2: _BaseNode):
        """ Helper function that adds a node between two other nodes. Time complexity: O(1).

        >>> node_1, node_2 = _Node(0), _Node(1)
        >>> node_1.next_node, node_2.previous_node = node_2, node_1
        >>> isinstance(node_1.next_node.next_node, _Node)
        False
        >>> PositionalLinkedList._insert_between(_Node(2), node_1, node_2)
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
        >>> PositionalLinkedList._remove_between(node_1, node_3)
        >>> isinstance(node_1.next_node.next_node, _Node)
        False
        """
        node1.next_node, node2.previous_node = node2, node1

    @staticmethod
    def _validate_node(node):
        """ Helper function that checks if a node is a sentinel. Returns None if the node is a sentinel, otherwise
        returns the node itself. Time complexity: O(1).

        >>> node_1, node_2 = _Node(0), _SentinelNode()
        >>> PositionalLinkedList._validate_node(node_1) is None
        False
        >>> PositionalLinkedList._validate_node(node_2) is None
        True
        """
        if isinstance(node, _SentinelNode):
            return None
        else:
            return node

    @staticmethod
    def _invalidate_position(variables):
        """ Helper function that sets the belongs_to key of a dictionary to None. Time complexity: O(1).

        >>> a_dict1 = {"belongs_to": 8, "dummy": 0}
        >>> a_dict1
        {'belongs_to': 8, 'dummy': 0}
        >>> a_dict2 = PositionalLinkedList._invalidate_position(a_dict1)
        >>> a_dict2
        {'belongs_to': None, 'dummy': 0}
        """
        variables["belongs_to"] = None
        return variables

    def is_empty(self):
        """ Returns True if list is empty, else False. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> l_list.is_empty()
        True
        >>> _ = l_list.append(1)
        >>> l_list.is_empty()
        False

        :return: True if list is empty, else False
        """
        return self.__length == 0

    def insert_first(self, data):
        """ Add item at the head of the list. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> _ = l_list.insert_first(0)
        >>> _ = l_list.insert_first(1)
        >>> l_list
        [1, 0]
        """
        self.__length += 1
        node = _Node(data)

        PositionalLinkedList._insert_between(node, self.__head, self.__head.next_node)

        return _Position(self, node)

    def insert_last(self, data):
        """ Add item at the tail of the list. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> _ = l_list.insert_last(0)
        >>> _ = l_list.insert_last(1)
        >>> l_list
        [0, 1]
        """
        self.__length += 1
        node = _Node(data)

        PositionalLinkedList._insert_between(node, self.__tail.previous_node, self.__tail)

        return _Position(self, node)

    def append(self, data):
        """ Alias of insert_last

        >>> l_list = PositionalLinkedList()
        >>> _ = l_list.append(0)
        >>> _ = l_list.append(1)
        >>> l_list
        [0, 1]
        """
        return self.insert_last(data)

    def insert_before(self, position: _Position, data):
        """ Add item before the defined position within the list. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> _ = l_list.insert_first(0)
        >>> _ = l_list.insert_first(1)
        >>> last = l_list.get_last()
        >>> _ = l_list.insert_before(last, 2)
        >>> l_list
        [1, 2, 0]
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

        self.__length += 1
        new_node = _Node(data)
        node = position.manipulate_node(self, "_validate_node", *[])

        PositionalLinkedList._insert_between(new_node, node.previous_node, node)

        return _Position(self, new_node)

    def insert_after(self, position: _Position, data):
        """ Add item after the defined position within the list. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> _ = l_list.insert_first(0)
        >>> _ = l_list.insert_first(1)
        >>> first = l_list.get_first()
        >>> _ = l_list.insert_after(first, 2)
        >>> l_list
        [1, 2, 0]
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

        self.__length += 1
        new_node = _Node(data)
        node = position.manipulate_node(self, "_validate_node", *[])

        PositionalLinkedList._insert_between(new_node, node, node.next_node)

        return _Position(self, new_node)

    def replace(self, position: _Position, data):
        """ Replaces item at a specific position. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> _ = l_list.append(0)
        >>> l_list
        [0]
        >>> first = l_list.get_first()
        >>> l_list.replace(first, 100)
        0
        >>> l_list
        [100]
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

        self.__length += 1
        node = position.manipulate_node(self, "_validate_node", *[])
        current_data = node.data
        node.data = data

        return current_data

    def remove(self, position: _Position):
        """ Deletes item at a specific position. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> _ = l_list.append(0)
        >>> l_list
        [0]
        >>> first = l_list.get_first()
        >>> l_list.remove(first)
        0
        >>> l_list
        []
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

        self.__length -= 1
        node = position.manipulate_node(self, "_validate_node", *[])
        _ = position.manipulate_variables(self, "_invalidate_position", *[])

        PositionalLinkedList._remove_between(node.previous_node, node.next_node)

        return node.data

    def get_first(self):
        """ Returns the position of the item at the head of the list. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> l_list.get_first() is None
        True
        >>> _ = l_list.append(0)
        >>> _ = l_list.append(1)
        >>> first = l_list.get_first()
        >>> first.get_data()
        0
        """
        if self.__length == 0:
            return None

        return _Position(self, self.__head.next_node)

    def get_last(self):
        """ Returns the position of the item at the tail of the list. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> l_list.get_last() is None
        True
        >>> _ = l_list.append(0)
        >>> _ = l_list.append(1)
        >>> last = l_list.get_last()
        >>> last.get_data()
        1
        """
        if self.__length == 0:
            return None

        return _Position(self, self.__tail.previous_node)

    def get_before(self, position: _Position):
        """ Returns the position just before the passed position. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> _ = l_list.append(0)
        >>> _ = l_list.append(1)
        >>> last = l_list.get_last()
        >>> before = l_list.get_before(last)
        >>> before.get_data()
        0
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

        node = position.manipulate_node(self, "_validate_node", *[])

        if node is None:
            return None
        elif isinstance(node.previous_node, _SentinelNode):
            return None
        else:
            return _Position(self, node.previous_node)

    def get_after(self, position: _Position):
        """ Returns the position just after the passed position. Time complexity: O(1).

        >>> l_list = PositionalLinkedList()
        >>> _ = l_list.append(0)
        >>> _ = l_list.append(1)
        >>> first = l_list.get_first()
        >>> after = l_list.get_after(first)
        >>> after.get_data()
        1
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

        node = position.manipulate_node(self, "_validate_node", *[])

        if node is None:
            return None
        elif isinstance(node.next_node, _SentinelNode):
            return None
        else:
            return _Position(self, node.next_node)
