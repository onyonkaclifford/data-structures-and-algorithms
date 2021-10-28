from abc import ABC, abstractmethod
from typing import Any, Generator, Iterable, List, Union


class Empty(Exception):
    pass


class Tree(ABC):
    """A tree is a hierarchical collection of nodes containing items, with each node having a unique parent and zero,
    one or many children items. The topmost element in a non-empty tree, the root, has no parent. Tree vocabularies
    include, but are not limited to:

    1. Root - the topmost element in a non-empty tree, it has no parent
    2. Leaf - a node with zero children
    3. Siblings - nodes that share a parent node
    4. Edge - a pair of nodes such the one is the parent of the other
    5. Path - a collection of nodes such that any pair of adjacent nodes have a parent/child relationship
    6. Height - number of edges between a node and it's furthest leaf
    7. Depth - number of edges between a node and the root
    8. Level - number of nodes in the path between a node and the root, inclusive of both the node itself and the root
    9. Ordered tree - a tree with a meaningful organisation among its nodes such that its nodes can be arranged in a
        linear manner from first to last
    """

    class _Node:
        def __init__(self, key, value, parent=None, children: Union[List, None] = None):
            self.key = key
            self.value = value
            self.parent = parent
            self.children = children if children is not None else []

    class _Position:
        """A representation of the position of a node within a tree"""

        def __init__(self, belongs_to, node):
            self.__variables = {"belongs_to": belongs_to}
            self.__node = node

        def is_owned_by(self, owner):
            """Check whether position belongs to the tree, owner. Time complexity: O(1).

            :param owner: object to check whether it's the owner of this position
            :returns: True of the position is owned by the object passed, else False
            """
            return owner is self.__variables["belongs_to"]

        def manipulate_variables(self, owner, method: str, *params):
            """Manipulate member variables of this position. Methods of the owner list are the only ones that can call
            this method. Time complexity: O(1).

            :param owner: tree object that owns this position
            :param method: method name of tree object that will manipulate the member variables of this position
            :param params: extra optional parameters to pass to the method
            :returns: the return value of the tree method whose name is passed
            """
            if not self.is_owned_by(owner):
                raise ValueError("Position doesn't belong to the passed owner")
            return getattr(owner, method)(self.__variables, *params)

        def manipulate_node(self, owner, method: str, *params):
            """Manipulate the node held by this position. Methods of the owner list are the only ones that can call
            this method. Time complexity: O(1).

            :param owner: tree object that owns this position
            :param method: method name of tree object that will manipulate the node contained in this position
            :param params: extra optional parameters to pass to the method
            :returns: the return value of the tree method whose name is passed
            """
            if not self.is_owned_by(owner):
                raise ValueError("Position doesn't belong to the passed owner")
            return getattr(owner, method)(self.__node, *params)

        def get_data(self):
            """Return the data stored by the node held by this position. Time complexity: O(1).

            :returns: data stored in node contained in this position
            """
            return self.__node.key, self.__node.value

    def __init__(self):
        self._root: Union[Tree._Node, None] = None
        self._length = 0
        self.__generator: Union[Generator, None] = None

    def __len__(self) -> int:
        """Return total number of items in tree

        :return: count of items in tree
        """
        return self._length

    def __repr__(self) -> str:
        """Return a string representation of the tree

        :return: the string representation of the tree
        """

        def helper(current_position):
            children = self.get_children(current_position)

            num_of_children = len(children)
            last_child_idx = num_of_children - 1

            data_dict["string_data"] += f"{current_position.get_data()[0]}"

            for i, j in enumerate(children):
                data_dict["string_data"] += "(" if i == 0 else ", "
                helper(j)
                data_dict["string_data"] += ")" if i == last_child_idx else ""

        if self.is_empty():
            return ""

        data_dict = {"string_data": ""}
        helper(Tree._Position(self, self._root))
        return data_dict["string_data"]

    def __iter__(self) -> Iterable:
        """Return a tree iterable

        :return: tree iterable
        """
        return self

    def __next__(self) -> _Position:
        """Return next position of tree iterator, implemented based on level-order traversal

        :return: next position
        :raises StopIteration: when the cursor denoting the current position surpasses the last position of the tree
        """
        if self.__generator is None:
            self.__generator = self.traverse_tree_level_order()

        try:
            next_position = next(self.__generator)
        except StopIteration as e:
            self.__generator = None
            raise e

        return next_position

    @staticmethod
    def _validate_node(node):
        """Helper function to check if the node passed is a tree node. Returns the node passed if the validation
        passes, else raises a TypeError. Time complexity: O(1).

        :param node: node to validate
        :returns: the node passed if it passes validation
        :raises TypeError: if the validation fails
        """
        if not isinstance(node, Tree._Node):
            raise TypeError("Not a tree node")
        return node

    @staticmethod
    def _invalidate_position(variables):
        """Helper function to set the belongs_to key of a dictionary to None. Used to revoke the ownership of a
        position by this tree. Time complexity: O(1).

        :returns: the dictionary passed, with the belongs_to key set to None
        """
        variables["belongs_to"] = None
        return variables

    def is_empty(self) -> bool:
        """Return True if tree is empty, else False. Time complexity: O(1).

        :returns: True if tree is empty, else False
        """
        return self._root is None

    def is_root(self, position: _Position) -> bool:
        """Check if the passed position contains the root node. Time complexity: O(1).

        :returns: True if the passed position holds the root node, else False
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")

        return node.parent is None

    def is_leaf(self, position: _Position) -> bool:
        """Check if the passed position contains a leaf. Time complexity: O(1).

        :returns: True if the passed position holds a leaf node, else False
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        return len(self.get_children(position)) == 0

    def get_root(self) -> Union[_Position, None]:
        """Return the root position. Time complexity: O(1).

        :returns: the root position
        """
        if self.is_empty():
            return None
        else:
            return Tree._Position(self, self._root)

    def get_parent(self, position: _Position) -> Union[_Position, None]:
        """Return the parent of the given position. Time complexity: O(1).

        :param position: position containing the node whose parent is being sought
        :returns: the position of parent of the node contained in the passed position. None if the position passed
        contains the root node.
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")

        if self.is_root(Tree._Position(self, node)):
            return None
        else:
            return Tree._Position(self, node.parent)

    def get_children(self, position: _Position) -> Union[List[_Position], None]:
        """Return the children of the given position. Time complexity: O(1).

        :param position: position containing the node whose children are being sought
        :returns: the positions of the children of the node contained in the passed position. None if the position has
        no children.
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")
        children = node.children

        if children is None:
            return None
        else:
            return [Tree._Position(self, i) for i in children if i is not None]

    def get_siblings(self, position: _Position) -> Union[List[_Position], None]:
        """Return the siblings of the given position. Time complexity: O(1).

        :param position: position containing the node whose children are being sought
        :returns: the positions of the siblings of the node contained in the passed position
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")
        parent = node.parent

        if parent is None:
            return []

        return [Tree._Position(self, i) for i in parent.children if i is not node]

    def get_height_of_node(self, position: _Position) -> int:
        """Return the number of edges between a node and the farthest leaf among its descendants. Time complexity:
        O(n).

        :param position: position containing the node whose height is being sought
        :returns: the number of edges between a node and the farthest leaf among its descendants
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        if self.is_leaf(position):
            return 0

        return 1 + max(self.get_height_of_node(p) for p in self.get_children(position))

    def get_height_of_tree(self) -> int:
        """Return the number of edges between the root node and the farthest leaf. Time complexity: O(n).

        :returns: the number of edges between the root node and the farthest leaf
        """
        if self.is_empty():
            raise Empty("Tree is empty")
        return self.get_height_of_node(Tree._Position(self, self._root))

    def get_depth_of_node(self, position: _Position) -> int:
        """Return the number of edges between a node and the root. Time complexity: O(n).

        :param position: position containing the node whose depth is being sought
        :returns: the number of edges between a node and the root
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        if self.is_root(position):
            return 0
        return 1 + self.get_depth_of_node(self.get_parent(position))

    def get_depth_of_tree(self) -> int:
        """Return the number of edges between the farthest leaf and the root. Time complexity: O(n).

        :returns: the number of edges between the farthest leaf and the root
        """
        return self.get_height_of_tree()

    def get_level_of_node(self, position: _Position) -> int:
        """Return the number of nodes between a node and the root, inclusive of itself. Time complexity: O(n).

        :param position: position containing the node whose level is being sought
        :returns: the number of nodes between a node and the root, inclusive of itself
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        return 1 + self.get_depth_of_node(position)

    def traverse_subtree_pre_order(self, position: _Position) -> Generator:
        """Pre-order traverse subtree whose root is the passed position and return a generator of the positions it
        contains

        :param position: position containing the node that's the root of the subtree to be traversed
        :returns: a generator of the positions
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        yield position
        for i in self.get_children(position):
            for j in self.traverse_subtree_pre_order(i):
                yield j

    def traverse_tree_pre_order(self) -> Generator:
        """Pre-order traverse tree and return a generator of the positions it contains

        :returns: a generator of the positions
        """
        position = self.get_root()

        if position is not None:
            for i in self.traverse_subtree_pre_order(position):
                yield i

    def traverse_subtree_post_order(self, position: _Position) -> Generator:
        """Post-order traverse subtree whose root is the passed position and return a generator of the positions it
        contains

        :param position: position containing the node that's the root of the subtree to be traversed
        :returns: a generator of the positions
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        for i in self.get_children(position):
            for j in self.traverse_subtree_post_order(i):
                yield j
        yield position

    def traverse_tree_post_order(self) -> Generator:
        """Post-order traverse tree and return a generator of the positions it contains

        :returns: a generator of the positions
        """
        position = self.get_root()

        if position is not None:
            for i in self.traverse_subtree_post_order(position):
                yield i

    def traverse_subtree_level_order(self, position: _Position) -> Generator:
        """Level-by-level traverse subtree whose root is the passed position and return a generator of the positions it
        contains

        :param position: position containing the node that's the root of the subtree to be traversed
        :returns: a generator of the positions
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        def helper(root_node, level):
            if root_node is not None:
                if level == 1:
                    yield Tree._Position(self, root_node)
                elif level > 1:
                    for child in root_node.children:
                        for k in helper(child, level - 1):
                            yield k

        node = position.manipulate_node(self, "_validate_node")
        number_of_levels = self.get_height_of_node(position) + 1

        for i in range(1, number_of_levels + 1):
            for j in helper(node, i):
                yield j

    def traverse_tree_level_order(self) -> Generator:
        """Level-by-level traverse tree and return a generator of the positions it contains

        :returns: a generator of the positions
        """
        position = self.get_root()

        if position is not None:
            for i in self.traverse_subtree_level_order(position):
                yield i

    def delete(self, position: _Position) -> None:
        """Delete a value from the tree

        :param position: position containing the node to be removed from the tree
        """
        self._length -= 1

        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        def insert_node(node_to_insert, is_node_left_child, parent_node):
            if node_to_insert is not None:
                node_to_insert.parent = parent_node
            if is_node_left_child is not None:
                if is_node_left_child:
                    parent_node.children[0] = node_to_insert
                else:
                    parent_node.children[1] = node_to_insert

        def delete_node(node_to_delete, is_root):
            parent = node_to_delete.parent
            left = node_to_delete.children[0]
            right = node_to_delete.children[1]
            is_left_child = None if parent is None else node_to_delete.key < parent.key

            if left is None:
                insert_node(right, is_left_child, parent)
                if is_root:
                    self._root = right
            else:
                current_node = left
                right_child = current_node.children[1]

                if right_child is None:
                    current_node.children[1] = right
                    insert_node(current_node, is_left_child, parent)
                    if is_root:
                        self._root = current_node
                else:
                    new_node = Tree._Node(
                        right_child.key,
                        right_child.value,
                        children=[current_node, right],
                    )

                    insert_node(new_node, is_left_child, parent)
                    if is_root:
                        self._root = new_node

                    delete_node(right_child, False)

        node = position.manipulate_node(self, "_validate_node")
        is_root_node = self.is_root(position)
        _ = position.manipulate_variables(self, "_invalidate_position")

        delete_node(node, is_root_node)

    @abstractmethod
    def insert(self, key: Any, value: Any) -> None:
        """Insert a value into the tree

        :param key: unique identifier of the item to be added to the tree
        :param value: item to be added to the tree
        """
        self._length += 1
