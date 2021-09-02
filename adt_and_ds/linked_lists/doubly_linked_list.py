from typing import Union
from linked_list import LinkedList, Empty


class DoublyLinkedList(LinkedList):
    """ A doubly linked list is a linear collection of nodes whose head and tail nodes are unconnected. Each node
    contains a reference to the node preceding it, and a reference to the node succeeding it.

    Instantiating a singly linked list
        >>> a_list = DoublyLinkedList()

    Appending an item to the list
        >>> a_list.append(0)

    The L.append(x) method is an alias of L.insert_last(x)
        >>> a_list.insert_last(1)

    Inserting an item at the head of the list
        >>> a_list.insert_first(2)

    Inserting an item at a specific index
        >>> a_list.insert(1, 3)

    Inserting an item at an index that's out of range raises an IndexError
        >>> a_list.insert(100, 3)
        Traceback (most recent call last):
        ...
        IndexError: Index out of range

    Get first item of the list
        >>> a_list.get_first()
        2

    Get first item of an empty list raises Empty
        >>> DoublyLinkedList().get_first()
        Traceback (most recent call last):
        ...
        linked_list.Empty: List is empty

    Get last item of the list
        >>> a_list.get_last()
        1

    Get last item of an empty list raises Empty
        >>> DoublyLinkedList().get_last()
        Traceback (most recent call last):
        ...
        linked_list.Empty: List is empty

    Get item at a specific index
        >>> a_list[1]
        3

    Get item at an index that's out of range raises an IndexError
        >>> a_list[100]
        Traceback (most recent call last):
        ...
        IndexError: Index out of range

    Get items at slice range of the list
        >>> a_list[1:3]
        [3, 0]

    Get items at a slice that's out of range raises an IndexError
        >>> a_list[1:100]
        Traceback (most recent call last):
        ...
        IndexError: Index out of range

    Get items at a slice with a slice step of less than one raises a ValueError
        >>> a_list[1:3:0]
        Traceback (most recent call last):
        ...
        ValueError: Step needs to be greater than zero

    Get an iterable object of the list
        >>> iterable_object = iter(a_list)

    Get next item of the iterable object
        >>> next(iterable_object)
        2

    Get next item of the list iterator
        >>> next(a_list)
        3

    Get length of the the list
        >>> len(a_list)
        4

    Get a string representation of the list
        >>> str(a_list)
        '[2, 3, 0, 1]'
        >>> a_list
        [2, 3, 0, 1]

    Delete first item of the list
        >>> a_list.remove_first()

    Delete first item of an empty list raises Empty
        >>> DoublyLinkedList().remove_first()
        Traceback (most recent call last):
        ...
        linked_list.Empty: List is empty

    Delete last item of the list
        >>> a_list.remove_last()

    Delete last item of an empty list raises Empty
        >>> DoublyLinkedList().remove_last()
        Traceback (most recent call last):
        ...
        linked_list.Empty: List is empty

    Delete item at a specific index
        >>> del a_list[0]

    Delete item of at an index that's out of range raises an IndexError
        >>> del a_list[100]
        Traceback (most recent call last):
        ...
        IndexError: Index out of range

    Replace item at a specific index
        >>> a_list[0] = 100

    Replace item of at an index that's out of range raises an IndexError
        >>> a_list[100] = 100
        Traceback (most recent call last):
        ...
        IndexError: Index out of range

    Delete all items from the list
        >>> a_list.remove_all()
        >>> a_list
        []
    """

    def __init__(self):
        super().__init__()
        self._head.next_node = self._tail
        self._tail.previous_node = self._head

    @staticmethod
    def _insert_between(
            new_node: LinkedList._Node,
            node1: Union[LinkedList._Node, LinkedList._SentinelNode],
            node2: Union[LinkedList._Node, LinkedList._SentinelNode]
    ):
        """ Helper function that inserts a node between two other nodes. Time complexity: O(1).

        :param new_node: node to be inserted
        :param node1: node at the start
        :param node2: node at the end
        """
        node1.next_node, new_node.next_node = new_node, node2
        new_node.previous_node, node2.previous_node = node1, new_node

    @staticmethod
    def _remove_between(
            node1: Union[LinkedList._Node, LinkedList._SentinelNode],
            node2: Union[LinkedList._Node, LinkedList._SentinelNode]
    ):
        """ Helper function that removes a node between two other nodes. Time complexity: O(1).

        :param node1: node at the start
        :param node2: node at the end
        """
        node1.next_node, node2.previous_node = node2, node1

    def insert_last(self, data):
        """ Add item at the tail of the list. Time complexity: O(1).

        :param data: item to insert
        """
        self._length += 1
        DoublyLinkedList._insert_between(LinkedList._Node(data), self._tail.previous_node, self._tail)

    def remove_last(self):
        """ Delete item at the tail of the list. Time complexity: O(1).

        :raises Empty: when the list is empty
        """
        if self._length == 0:
            raise Empty("List is empty")

        self._length -= 1
        current_node = self._tail.previous_node
        previous_node = current_node.previous_node

        DoublyLinkedList._remove_between(previous_node, self._tail)

    def get_last(self):
        """ Returns item at the tail of the list. Time complexity: O(1).

        :return: last item in list
        :raises Empty: when the list is empty
        """
        if self._length == 0:
            raise Empty("List is empty")

        return self._tail.previous_node.data
