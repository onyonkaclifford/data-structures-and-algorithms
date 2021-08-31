from typing import Union


class Empty(Exception):
    pass


class BinarySearchTree:
    class _Node:
        def __init__(self, data, parent=None, left=None, right=None):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right

    class _Position:
        """ A representation of the position of a node within a tree """

        def __init__(self, belongs_to, node):
            self.__variables = {"belongs_to": belongs_to}
            self.__node = node

        def is_owned_by(self, owner):
            """ Check whether position belongs to the tree, owner. Time complexity: O(1).

            >>> tree1, tree2 = BinarySearchTree(), BinarySearchTree()
            >>> tree1.insert(0)
            >>> position1 = tree1.get_root()
            >>> position1.is_owned_by(tree1)
            True
            >>> position1.is_owned_by(tree2)
            False
            """
            return owner is self.__variables["belongs_to"]

        def manipulate_variables(self, owner, method: str, *params):
            """ Manipulate member variables of this position. Methods of the owner list are the only ones that can call
            this method. Time complexity: O(1).

            >>> tree1, tree2 = BinarySearchTree(), BinarySearchTree()
            >>> tree1.insert(0)
            >>> position1 = tree1.get_root()
            >>> position1.manipulate_variables(tree2, "dummy_method", "param1", "param2")
            Traceback (most recent call last):
            ...
            ValueError: Position doesn't belong to the passed owner
            """
            if not self.is_owned_by(owner):
                raise ValueError("Position doesn't belong to the passed owner")
            return getattr(owner, method)(self.__variables, *params)

        def manipulate_node(self, owner, method: str, *params):
            """ Manipulate the node held by this position. Methods of the owner list are the only ones that can call
            this method. Time complexity: O(1).

            >>> tree1, tree2 = BinarySearchTree(), BinarySearchTree()
            >>> tree1.insert(0)
            >>> position1 = tree1.get_root()
            >>> position1.manipulate_node(tree2, "dummy_method", "param1", "param2")
            Traceback (most recent call last):
            ...
            ValueError: Position doesn't belong to the passed owner
            """
            if not self.is_owned_by(owner):
                raise ValueError("Position doesn't belong to the passed owner")
            return getattr(owner, method)(self.__node, *params)

        def get_data(self):
            """ Returns the data stored by the node held by this position. Time complexity: O(1).

            >>> tree1 = BinarySearchTree()
            >>> tree1.insert(0)
            >>> position1 = tree1.get_root()
            >>> position1.get_data()
            0
            """
            return self.__node.data

    def __init__(self):
        self.__root: Union[BinarySearchTree._Node, None] = None

    def __repr__(self):
        """ Returns a string representation of the tree. Time complexity: O(n).

        >>> tree = BinarySearchTree()
        >>> tree
        <BLANKLINE>
        >>> tree.insert(4)
        >>> tree
        4
        >>> tree.insert(2)
        >>> tree.insert(3)
        >>> tree.insert(1)
        >>> tree.insert(6)
        >>> tree.insert(7)
        >>> tree.insert(5)
        >>> tree
        4(2(1, 3), 6(5, 7))

        :return: string representation of the tree
        """
        def helper(current_position):
            left_child = self.get_left_child(current_position)
            right_child = self.get_right_child(current_position)
            children = []

            if left_child is not None:
                children.append(left_child)
            if right_child is not None:
                children.append(right_child)

            num_of_children = len(children)
            last_child_idx = num_of_children - 1

            data_dict["string_data"] += f"{current_position.get_data()}"

            for i, j in enumerate(children):
                data_dict["string_data"] += "(" if i == 0 else ", "
                helper(j)
                data_dict["string_data"] += ")" if i == last_child_idx else ""

        if self.is_empty():
            return ""

        data_dict = {"string_data": ""}
        helper(BinarySearchTree._Position(self, self.__root))
        return data_dict["string_data"]

    @staticmethod
    def _validate_node(node):
        """ Helper function that checks if the node passed is a tree node. Returns the node passed if the validation
        passes, elses raises a TypeError. Time complexity: O(1).

        >>> node_1, node_2 = BinarySearchTree._Node(0), object()
        >>> BinarySearchTree._validate_node(node_1) is node_1
        True
        >>> BinarySearchTree._validate_node(node_2) is node_2
        Traceback (most recent call last):
        ...
        TypeError: Not a tree node
        """
        if not isinstance(node, BinarySearchTree._Node):
            raise TypeError("Not a tree node")
        return node

    @staticmethod
    def _invalidate_position(variables):
        """ Helper function that sets the belongs_to key of a dictionary to None. Time complexity: O(1).

        >>> a_dict1 = {"belongs_to": 8, "dummy": 0}
        >>> a_dict1
        {'belongs_to': 8, 'dummy': 0}
        >>> a_dict2 = BinarySearchTree._invalidate_position(a_dict1)
        >>> a_dict2
        {'belongs_to': None, 'dummy': 0}
        """
        variables["belongs_to"] = None
        return variables

    def is_empty(self):
        """ Returns True if tree is empty, else False. Time complexity: O(1).

        >>> tree = BinarySearchTree()
        >>> tree.is_empty()
        True
        >>> tree.insert(1)
        >>> tree.is_empty()
        False

        :return: True if tree is empty, else False
        """
        return self.__root is None

    def is_root(self, position: _Position):
        """ Returns True if the passed position holds the root node, else False. Time complexity: O(1).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> root = tree.get_root()
        >>> right = tree.get_right_child(root)
        >>> tree.is_root(root)
        True
        >>> tree.is_root(right)
        False
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")

        return node is self.__root

    def is_leaf(self, position: _Position):
        """ Returns True if the passed position holds a leaf node, else False. Time complexity: O(1).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> root = tree.get_root()
        >>> right = tree.get_right_child(root)
        >>> tree.is_leaf(root)
        False
        >>> tree.is_leaf(right)
        True
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node",)

        return node.left is None and node.right is None

    def get_root(self):
        """ Returns the root position. Time complexity: O(1).

        >>> tree = BinarySearchTree()
        >>> tree.get_root() is None
        True
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> root = tree.get_root()
        >>> tree.is_root(root)
        True
        """
        if self.is_empty():
            return None
        else:
            return BinarySearchTree._Position(self, self.__root)

    def get_parent(self, position: _Position):
        """ Returns the parent of the given position. Time complexity: O(1).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> root = tree.get_root()
        >>> right = tree.get_right_child(root)
        >>> parent = tree.get_parent(right)
        >>> parent.get_data()
        1
        >>> tree.get_parent(root) is None
        True
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")

        if self.is_root(BinarySearchTree._Position(self, node)):
            return None
        else:
            return BinarySearchTree._Position(self, node.parent)

    def get_left_child(self, position: _Position):
        """ Returns the left child of the given position. Time complexity: O(1).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> root = tree.get_root()
        >>> left = tree.get_left_child(root)
        >>> left.get_data()
        0
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")

        if node.left is None:
            return None
        else:
            return BinarySearchTree._Position(self, node.left)

    def get_right_child(self, position: _Position):
        """ Returns the right child of the given position. Time complexity: O(1).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> root = tree.get_root()
        >>> right = tree.get_right_child(root)
        >>> right.get_data()
        2
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")

        if node.right is None:
            return None
        else:
            return BinarySearchTree._Position(self, node.right)

    def get_sibling(self, position: _Position):
        """ Returns the sibling of the given position. Time complexity: O(1).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> root = tree.get_root()
        >>> left = tree.get_left_child(root)
        >>> right = tree.get_right_child(root)
        >>> tree.get_sibling(left).get_data()
        2
        >>> tree.get_sibling(right).get_data()
        0
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")
        parent = node.parent

        return BinarySearchTree._Position(self, parent.left) if node is not parent.left else \
            BinarySearchTree._Position(self, parent.right)

    def get_height_of_node(self, position: _Position):
        """ Returns the number of edges between a node and the farthest leaf among its descendants. Time complexity:
        O(n).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> root = tree.get_root()
        >>> tree.get_height_of_node(root)
        1
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        if self.is_leaf(position):
            return 0

        children = []
        left = self.get_left_child(position)
        right = self.get_right_child(position)

        if left is not None:
            children.append(left)
        if right is not None:
            children.append(right)

        return 1 + max(self.get_height_of_node(p) for p in children)

    def get_height_of_tree(self):
        """ Returns the number of edges between the root node and the farthest leaf. Time complexity: O(n).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> tree.get_height_of_tree()
        1
        """
        if self.is_empty():
            raise Empty("Tree is empty")
        return self.get_height_of_node(BinarySearchTree._Position(self, self.__root))

    def get_depth_of_node(self, position: _Position):
        """ Returns the number of edges between a node and the root. Time complexity: O(n).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> root = tree.get_root()
        >>> left = tree.get_left_child(root)
        >>> tree.get_depth_of_node(left)
        1
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        if self.is_root(position):
            return 0
        return 1 + self.get_depth_of_node(self.get_parent(position))

    def get_depth_of_tree(self):
        """ Returns the number of edges between the root and the farthest leaf. Time complexity: O(n).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> tree.get_depth_of_tree()
        1
        """
        return self.get_height_of_tree()

    def get_level_of_node(self, position: _Position):
        """ Returns the number of nodes between a node and the root, inclusive of itself. Time complexity: O(n).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> root = tree.get_root()
        >>> left = tree.get_left_child(root)
        >>> tree.get_level_of_node(left)
        2
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        return 1 + self.get_depth_of_node(position)

    def get_highest(self):
        """ Returns the highest value in the tree. Time complexity: O(n).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> tree.get_highest().get_data()
        2
        """
        if self.is_empty():
            raise Empty("Tree is empty")

        current_node = self.__root

        while current_node.right is not None:
            current_node = current_node.right

        return BinarySearchTree._Position(self, current_node)

    def get_lowest(self):
        """ Returns the lowest value in the tree. Time complexity: O(n).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> tree.get_lowest().get_data()
        0
        """
        if self.is_empty():
            raise Empty("Tree is empty")

        current_node = self.__root

        while current_node.left is not None:
            current_node = current_node.left

        return BinarySearchTree._Position(self, current_node)

    def insert(self, data):
        """ Inserts a value into the tree. Time complexity: O(n).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> tree
        1(0, 2)
        """
        node = BinarySearchTree._Node(data)
        if self.is_empty():
            self.__root = node
        else:
            current_node = self.__root
            previous_node = current_node.parent

            while current_node is not None:
                previous_node = current_node
                if data == current_node.data:
                    raise ValueError("Data already exists in tree")
                elif data > current_node.data:
                    current_node = current_node.right
                else:
                    current_node = current_node.left

            node.parent = previous_node
            if data > previous_node.data:
                previous_node.right = node
            else:
                previous_node.left = node

    def delete(self, position: _Position):
        """ Deletes a value from the tree.

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> tree
        1(0, 2)
        >>> root = tree.get_root()
        >>> right = tree.get_right_child(root)
        >>> tree.delete(right)
        >>> tree
        1(0)
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        def insert_node(node_to_insert, is_node_left_child, parent_node):
            if node_to_insert is not None:
                node_to_insert.parent = parent_node
            if is_node_left_child:
                parent_node.left = node_to_insert
            else:
                parent_node.right = node_to_insert

        def delete_node(node_to_delete):
            parent = node_to_delete.parent
            is_left_child = node_to_delete.data < parent.data

            if node_to_delete.left is None:
                insert_node(node_to_delete.right, is_left_child, parent)
            else:
                current_node = node_to_delete.left
                right_child = current_node.right

                if right_child is None:
                    current_node.right = node_to_delete.right
                    insert_node(current_node, is_left_child, parent)
                else:
                    new_node = BinarySearchTree._Node(right_child.data, left=current_node, right=node_to_delete.right)

                    insert_node(new_node, is_left_child, parent)
                    delete_node(right_child)

        node = position.manipulate_node(self, "_validate_node")
        _ = position.manipulate_variables(self, "_invalidate_position")

        delete_node(node)

    def search(self, data):
        """ Returns the position of a value within the tree, or None if the value doesn't exist in the tree. Time
        complexity: O(n).

        >>> tree = BinarySearchTree()
        >>> tree.insert(1)
        >>> tree.insert(2)
        >>> tree.insert(0)
        >>> tree.search(100) is None
        True
        >>> tree.search(2).get_data()
        2
        """
        if self.is_empty():
            raise Empty("Tree is empty")

        current_node = self.__root

        while current_node is not None:
            if data == current_node.data:
                break
            elif data > current_node.data:
                current_node = current_node.right
            else:
                current_node = current_node.left

        if current_node is None:
            return None
        else:
            return BinarySearchTree._Position(self, current_node)
