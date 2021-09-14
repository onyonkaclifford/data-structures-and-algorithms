from abc import ABC, abstractmethod


class PositionalLinkedList(ABC):
    """ A positional linked list is a linked list whose nodes are identifiable by their position within the list. Using
    the position of a node, operations such as insertion, retrieval, and deletion of elements can be performed on
    neighbouring nodes without the need to traverse the list from its head or tail to that specific position.

    A positional linked list can be implemented based on any linked list data structure, such as singly linked list,
    doubly linked list, etc. The operations that can be performed on the neighbouring nodes of a certain position are
    limited to the directions of traversal offered by the data structure used to implement the positional linked list.
    When using a linked list data structure where each node has a reference to the node succeeding it but not the one
    preceding it, only operations referencing the next neighbours of a specific position are achievable. If the linked
    data structure contains nodes where each node contains references to both its previous and next nodes, operations
    referencing both the previous and next neighbours of a specific position are achievable.
    """

    class _Position:
        """ A representation of the position of a node within a positional linked list """

        def __init__(self, belongs_to, node):
            self.__variables = {"belongs_to": belongs_to}
            self.__node = node

        def is_owned_by(self, owner):
            """ Check whether position belongs to the list, owner. Time complexity: O(1).

            :param owner: object to check whether it's the owner of this position
            :returns: True of the position is owned by the object passed, else False
            """
            return owner is self.__variables["belongs_to"]

        def manipulate_variables(self, owner, method: str, *params):
            """ Manipulate member variables of this position. Methods of the owner list are the only ones that can call
            this method. Time complexity: O(1).

            :param owner: list object that owns this position
            :param method: method name of list object that will manipulate the member variables of this position
            :param params: extra optional parameters to pass to the method
            :returns: the return value of the list method whose name is passed
            """
            if not self.is_owned_by(owner):
                raise ValueError("Position doesn't belong to the passed owner")
            return getattr(owner, method)(self.__variables, *params)

        def manipulate_node(self, owner, method: str, *params):
            """ Manipulate the node held by this position. Methods of the owner list are the only ones that can call this
            method. Time complexity: O(1).

            :param owner: list object that owns this position
            :param method: method name of list object that will manipulate the node contained in this position
            :param params: extra optional parameters to pass to the method
            :returns: the return value of the list method whose name is passed
            """
            if not self.is_owned_by(owner):
                raise ValueError("Position doesn't belong to the passed owner")
            return getattr(owner, method)(self.__node, *params)

        def get_data(self):
            """ Returns the data stored by the node held by this position. Time complexity: O(1).

            :returns: data stored in node contained in this position
            """
            return self.__node.data

    @staticmethod
    def _invalidate_position(variables):
        """ Helper function that sets the belongs_to key of a dictionary to None. Time complexity: O(1).

        :returns: the passed dictionary with belongs_to set to None
        """
        variables["belongs_to"] = None
        return variables

    @staticmethod
    @abstractmethod
    def _validate_node(node):
        """ Helper function that checks if a node is a sentinel. Returns None if the node is a sentinel, otherwise
        returns the node itself. Time complexity: O(1).

        :param node: node to validate
        :returns: None if the node passed is a sentinel node, else returns the node that was passed
        """
        raise NotImplementedError

    @abstractmethod
    def is_empty(self):
        """ Returns True if list is empty, else False

        :return: True if list is empty, else False
        """
        raise NotImplementedError

    @abstractmethod
    def insert_before(self, position: _Position, data):
        """ Add item before the defined position within the list

        :param position: reference position
        :param data: item to insert
        :returns: the position of the added item
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

    @abstractmethod
    def insert_after(self, position: _Position, data):
        """ Add item after the defined position within the list

        :param position: reference position
        :param data: item to insert
        :returns: the position of the added item
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

    @abstractmethod
    def get_before(self, position: _Position):
        """ Returns the position just before the passed position

        :param position: reference position
        :returns: the position just before the passed position
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

    @abstractmethod
    def get_after(self, position: _Position):
        """ Returns the position just after the passed position

        :param position: reference position
        :returns: the position just after the passed position
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

    @abstractmethod
    def remove_before(self, position: _Position):
        """ Deletes item just before the passed position

        :param position: reference position
        :returns: the deleted item
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

    @abstractmethod
    def remove_after(self, position: _Position):
        """ Deletes item just after the passed position

        :param position: reference position
        :returns: the deleted item
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

    @abstractmethod
    def remove(self, position: _Position):
        """ Deletes item at a specific position

        :param position: position containing item to be deleted
        :returns: the deleted item
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

    @abstractmethod
    def insert_first(self, data):
        """ Add item at the head of the list

        :param data: item to insert
        :returns: the position of the added item
        """
        raise NotImplementedError

    @abstractmethod
    def insert_last(self, data):
        """ Add item at the tail of the list

        :param data: item to insert
        :returns: the position of the added item
        """
        raise NotImplementedError

    def append(self, data):
        """ Alias of insert_last

        :param data: item to insert
        """
        return self.insert_last(data)

    @abstractmethod
    def get_first(self):
        """ Returns the position of the item at the head of the list

        :returns: the position of the item at the head of the list
        """
        raise NotImplementedError

    @abstractmethod
    def get_last(self):
        """ Returns the position of the item at the tail of the list

        :returns: the position of the item at the tail of the list
        """
        raise NotImplementedError

    def remove_first(self):
        """ Delete item at the head of the list

        :returns: the deleted item
        """
        raise NotImplementedError

    @abstractmethod
    def remove_last(self):
        """ Delete item at the tail of the list

        :returns: the deleted item
        """
        raise NotImplementedError

    def replace(self, position: _Position, data):
        """ Replaces item at a specific position. Time complexity: O(1).

        :param position: reference position
        :param data: item to replace the existing item at the reference position
        :returns: the item replaced from the reference position
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this list")

        node = position.manipulate_node(self, "_validate_node", *[])
        current_data = node.data
        node.data = data

        return current_data
