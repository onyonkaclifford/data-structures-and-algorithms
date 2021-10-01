from abc import abstractmethod

from tree import Tree


class BinaryTree(Tree):
    """A binary tree is a tree whose nodes contain a maximum of two children, the left child and the right child. The
    order of the children of any node is such that the left child has precedence over the right child. Binary tree
    vocabularies include, but are not limited to:

    1. Proper/full binary tree - a binary tree whose nodes each have zero or two children
    2. Balanced binary tree - a binary tree whose left and right subtrees heights differ by a maximum of one, with each
        of the left and right subtrees being recursively balanced
    3. Complete binary tree - a binary tree whose levels are completely filled, except possibly for the last level whose
        nodes must be as far left as possible
    4. Perfect binary tree - a binary tree whose internal nodes each contain two children, and the leaves are contained
        within the same level
    """

    def __init__(self):
        super().__init__()

    def get_left_child(self, position: Tree._Position):
        """Returns the left child of the given position. Time complexity: O(1).

        :param position: position containing the node whose left child is being sought
        :returns: the position of the left child of the node contained in the passed position. None if the position has
        no left child.
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")
        children = node.children

        if children is None:
            return None
        else:
            left_child = children[0]
            return Tree._Position(self, left_child) if left_child is not None else None

    def get_right_child(self, position: Tree._Position):
        """Returns the right child of the given position. Time complexity: O(1).

        :param position: position containing the node whose right child is being sought
        :returns: the position of the right child of the node contained in the passed position. None if the position has
        no right child.
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        node = position.manipulate_node(self, "_validate_node")
        children = node.children

        if children is None:
            return None
        else:
            right_child = children[1]
            return (
                Tree._Position(self, right_child) if right_child is not None else None
            )

    def traverse_subtree_in_order(self, position: Tree._Position):
        """In-order traverse subtree whose root is the passed position and return a generator of the positions it
        contains. Time complexity: O(1).

        :param position: position containing the node that's the root of the subtree to be traversed
        :returns: a generator of the positions
        """
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        left_child = self.get_left_child(position)
        right_child = self.get_right_child(position)

        if left_child is not None:
            for i in self.traverse_subtree_in_order(left_child):
                yield i

        yield position

        if right_child is not None:
            for i in self.traverse_subtree_in_order(right_child):
                yield i

    def traverse_tree_in_order(self):
        """In-order traverse tree and return a generator of the positions it contains. Time complexity: O(1).

        :returns: a generator of the positions
        """
        position = self.get_root()

        if position is not None:
            for i in self.traverse_subtree_in_order(position):
                yield i

    @abstractmethod
    def insert(self, data):
        super().insert(data)
