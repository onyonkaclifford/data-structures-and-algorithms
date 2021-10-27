from singly_linked_list import SinglyLinkedList


class CircularlySinglyLinkedList(SinglyLinkedList):
    """A circularly singly linked list is a cyclic collection of nodes whose head and tail nodes are connected. Each
    node contains a reference to the node succeeding it.

    Instantiate a circularly singly linked list object

        >>> a_list = CircularlySinglyLinkedList()

    Append an item to the list

        >>> a_list.append(0)

    The L.append(x) method is an alias of L.insert_last(x)

        >>> a_list.insert_last(1)

    Insert an item at the head of the list

        >>> a_list.insert_first(2)

    Insert an item at a specific index

        >>> a_list.insert(1, 3)

    Insert an item at an index that's out of range raises IndexError

        >>> a_list.insert(100, 3)
        Traceback (most recent call last):
        ...
        IndexError: Index out of range

    Get first item of the list

        >>> a_list.get_first()
        2

    Get first item of an empty list raises Empty

        >>> CircularlySinglyLinkedList().get_first()
        Traceback (most recent call last):
        ...
        linked_list.Empty: List is empty

    Get last item of the list

        >>> a_list.get_last()
        1

    Get last item of an empty list raises Empty

        >>> CircularlySinglyLinkedList().get_last()
        Traceback (most recent call last):
        ...
        linked_list.Empty: List is empty

    Get item at a specific index

        >>> a_list[1]
        3

    Get item at an index that's out of range raises IndexError

        >>> a_list[100]
        Traceback (most recent call last):
        ...
        IndexError: Index out of range

    Get items at slice range of the list

        >>> a_list[1:3]
        [3, 0]

    Get items at a slice that's out of range raises IndexError

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

        >>> CircularlySinglyLinkedList().remove_first()
        Traceback (most recent call last):
        ...
        linked_list.Empty: List is empty

    Delete last item of the list

        >>> a_list.remove_last()

    Delete last item of an empty list raises Empty

        >>> CircularlySinglyLinkedList().remove_last()
        Traceback (most recent call last):
        ...
        linked_list.Empty: List is empty

    Delete item at a specific index

        >>> del a_list[0]

    Delete item of at an index that's out of range raises IndexError

        >>> del a_list[100]
        Traceback (most recent call last):
        ...
        IndexError: Index out of range

    Replace item at a specific index

        >>> a_list[0] = 100

    Replace item of at an index that's out of range raises IndexError

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
        self._tail.next_node = self._head
