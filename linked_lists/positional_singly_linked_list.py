from positional_linked_list import PositionalLinkedList
from singly_linked_list import SinglyLinkedList


class PositionalSinglyLinkedList(PositionalLinkedList, SinglyLinkedList):
    """ A positional singly linked list is a positional list implemented based on a singly linked list.

    Instantiating a positional singly linked list
        >>> a_list = PositionalSinglyLinkedList()

    Appending an item to the list
        >>> position = a_list.append(0)
        >>> position.get_data()
        0

    The L.append(x) method is an alias of L.insert_last(x)
        >>> position = a_list.insert_last(1)
        >>> position.get_data()
        1

    Inserting an item at the head of the list
        >>> position = a_list.insert_first(2)
        >>> position.get_data()
        2

    Inserting an item just before a certain position in the list
        >>> new_position = a_list.insert_before(position, 3)
        >>> new_position.get_data()
        3

    Inserting an item just after a certain position in the list
        >>> new_position = a_list.insert_after(position, 4)
        >>> new_position.get_data()
        4

    Replace item at a specific position
        >>> a_list.replace(position, 100)
        2

    Checking if a positional singly linked list is empty
        >>> a_list.is_empty()
        False
        >>> PositionalSinglyLinkedList().is_empty()
        True

    Get first item of the list
        >>> position = a_list.get_first()
        >>> position.get_data()
        3

    Get last item of the list
        >>> position = a_list.get_last()
        >>> position.get_data()
        1

    Get item just before a certain position of the list
        >>> position = a_list.get_last()
        >>> before_position = a_list.get_before(position)
        >>> before_position.get_data()
        0

    Get item just after a certain position of the list
        >>> position = a_list.get_first()
        >>> after_position = a_list.get_after(position)
        >>> after_position.get_data()
        100

    Delete item just before a certain position from the list
        >>> a_list.remove_before(after_position)
        3

    Delete item just after a certain position from the list
        >>> a_list.remove_after(after_position)
        4

    Delete item in a certain position from the list
        >>> position = a_list.get_first()
        >>> a_list.remove(position)
        100

    Delete first item from the list
        >>> a_list.remove_first()
        0

    Delete last item from the list
        >>> a_list.remove_last()
        1
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def _validate_node(node):
        if isinstance(node, SinglyLinkedList._SentinelNode):
            return None
        else:
            return node

    def is_empty(self):
        return self._length == 0

    def insert_before(self, position: PositionalLinkedList._Position, data):
        super().insert_before(position, data)

        self._length += 1
        new_node = SinglyLinkedList._Node(data)
        node = position.manipulate_node(self, "_validate_node", *[])

        previous_node = self._head
        current_node = previous_node.next_node

        while current_node.data != node.data:
            previous_node = current_node
            current_node = current_node.next_node

        SinglyLinkedList._insert_between(new_node, previous_node, node)

        return PositionalLinkedList._Position(self, new_node)

    def insert_after(self, position: PositionalLinkedList._Position, data):
        super().insert_after(position, data)

        self._length += 1
        new_node = SinglyLinkedList._Node(data)
        node = position.manipulate_node(self, "_validate_node", *[])

        SinglyLinkedList._insert_between(new_node, node, node.next_node)

        return PositionalLinkedList._Position(self, new_node)

    def get_before(self, position: PositionalLinkedList._Position):
        super().get_before(position)

        node = position.manipulate_node(self, "_validate_node", *[])
        if node is None:
            return None

        previous_node = self._head
        current_node = previous_node.next_node

        while current_node.data != node.data:
            previous_node = current_node
            current_node = current_node.next_node

        if isinstance(previous_node, SinglyLinkedList._SentinelNode):
            return None
        else:
            return PositionalLinkedList._Position(self, previous_node)

    def get_after(self, position: PositionalLinkedList._Position):
        super().get_after(position)

        node = position.manipulate_node(self, "_validate_node", *[])
        if node is None:
            return None

        node_to_get = node.next_node
        if isinstance(node_to_get, SinglyLinkedList._SentinelNode):
            return None
        else:
            return PositionalLinkedList._Position(self, node_to_get)

    def remove_before(self, position: PositionalLinkedList._Position):
        super().remove_before(position)

        node = position.manipulate_node(self, "_validate_node", *[])

        pre_previous_node = None
        previous_node = self._head
        current_node = previous_node.next_node

        while current_node.data != node.data:
            pre_previous_node = previous_node
            previous_node = current_node
            current_node = current_node.next_node

        if isinstance(previous_node, SinglyLinkedList._SentinelNode):
            return None

        self._length -= 1
        SinglyLinkedList._remove_between(pre_previous_node, node)

        return previous_node.data

    def remove_after(self, position: PositionalLinkedList._Position):
        super().remove_after(position)

        node = position.manipulate_node(self, "_validate_node", *[])
        node_to_delete = node.next_node

        if isinstance(node_to_delete, SinglyLinkedList._SentinelNode):
            return None

        self._length -= 1
        SinglyLinkedList._remove_between(node, node_to_delete.next_node)

        return node_to_delete.data

    def remove(self, position: PositionalLinkedList._Position):
        super().remove(position)

        self._length -= 1
        node = position.manipulate_node(self, "_validate_node", *[])
        _ = position.manipulate_variables(self, "_invalidate_position", *[])

        previous_node = self._head
        current_node = previous_node.next_node

        while current_node.data != node.data:
            previous_node = current_node
            current_node = current_node.next_node

        SinglyLinkedList._remove_between(previous_node, node.next_node)

        return node.data

    def insert_first(self, data):
        SinglyLinkedList.insert_first(self, data)
        return PositionalLinkedList._Position(self, self._head.next_node)

    def insert_last(self, data):
        SinglyLinkedList.insert_last(self, data)

        current_node = self._head.next_node

        while not isinstance(current_node.next_node, SinglyLinkedList._SentinelNode):
            current_node = current_node.next_node

        return PositionalLinkedList._Position(self, current_node)

    def get_first(self):
        if self._length == 0:
            return None

        return PositionalLinkedList._Position(self, self._head.next_node)

    def get_last(self):
        if self._length == 0:
            return None

        current_node = self._head.next_node

        while not isinstance(current_node.next_node, SinglyLinkedList._SentinelNode):
            current_node = current_node.next_node

        return PositionalLinkedList._Position(self, current_node)

    def remove_first(self):
        if self._length == 0:
            return None

        node_to_delete = self._head.next_node

        SinglyLinkedList.remove_first(self)

        return node_to_delete.data

    def remove_last(self):
        if self._length == 0:
            return None

        node_to_delete = self._head.next_node

        while not isinstance(node_to_delete.next_node, SinglyLinkedList._SentinelNode):
            node_to_delete = node_to_delete.next_node

        SinglyLinkedList.remove_last(self)

        return node_to_delete.data
