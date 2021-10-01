from binary_tree import BinaryTree
from tree import Empty, Tree


class BinarySearchTree(BinaryTree):
    """A binary search tree is a binary tree whose left child of each node contain an item less in value than itself,
    and the right child an item higher in value than itself. An in-order traversal of the binary search tree results
    to items arranged in ascending order.

    Instantiating a binary search tree
        >>> tree = BinarySearchTree()

    Inserting an item to the tree
        >>> tree.insert(5)
        >>> tree.insert(4)
        >>> tree.insert(6)
        >>> tree.insert(10)

    Check if a tree is empty
        >>> tree.is_empty()
        False
        >>> BinarySearchTree().is_empty()
        True

    Get root position
        >>> root = tree.get_root()

    Get item corresponding to a certain position
        >>> root.get_data()
        5

    Check if a position is owned by some tree
        >>> root.is_owned_by(tree)
        True
        >>> root.is_owned_by(BinarySearchTree())
        False

    Get children of some position
        >>> children = tree.get_children(root)
        >>> [i.get_data() for i in children]
        [4, 6]

    Get left child of some position
        >>> left_child = tree.get_left_child(root)
        >>> left_child.get_data()
        4

    Get right child of some position
        >>> right_child = tree.get_right_child(root)
        >>> right_child.get_data()
        6

    Deleting an item from the tree
        >>> position_to_delete = tree.get_right_child(right_child)
        >>> tree.delete(position_to_delete)

    Check if a position contains the root
        >>> tree.is_root(root)
        True
        >>> tree.is_root(left_child)
        False

    Check if a position contains a leaf node
        >>> tree.is_leaf(left_child)
        True
        >>> tree.is_leaf(root)
        False

    Get parent of some position
        >>> tree.get_parent(left_child).get_data()
        5
        >>> tree.get_parent(root) is None
        True

    Get siblings of some position
        >>> siblings = tree.get_siblings(left_child)
        >>> [i.get_data() for i in siblings]
        [6]

    Get height of some position
        >>> tree.get_height_of_node(left_child)
        0
        >>> tree.get_height_of_node(root)
        1

    Get height of tree
        >>> tree.get_height_of_tree()
        1

    Get depth of some position
        >>> tree.get_depth_of_node(left_child)
        1
        >>> tree.get_depth_of_node(root)
        0

    Get depth of tree
        >>> tree.get_depth_of_tree()
        1

    Get level of some position
        >>> tree.get_level_of_node(left_child)
        2
        >>> tree.get_level_of_node(root)
        1

    Get length of tree
        >>> len(tree)
        3
        >>> len(BinarySearchTree())
        0

    Get string reresentation of tree
        >>> tree
        5(4, 6)
        >>> str(tree)
        '5(4, 6)'

    Get tree iterable
        >>> tree_iterable = iter(tree)
        >>> next(tree_iterable).get_data()
        5

    Get next item of tree iterator
        >>> next(tree).get_data()
        4
    """

    def __init__(self):
        super().__init__()

    def insert(self, data):
        super().insert(data)

        node = Tree._Node(data, children=[None, None])

        if self.is_empty():
            self._root = node
        else:
            current_node = self._root
            previous_node = current_node.parent

            while current_node is not None:
                previous_node = current_node
                left_child = current_node.children[0]
                right_child = current_node.children[1]
                if data == current_node.data:
                    raise ValueError("Data already exists in tree")
                elif data > current_node.data:
                    current_node = right_child
                else:
                    current_node = left_child

            node.parent = previous_node
            if data > previous_node.data:
                previous_node.children[1] = node
            else:
                previous_node.children[0] = node

    def search(self, data):
        """Returns the position of a value within the tree, or None if the value doesn't exist in the tree. Time
        complexity: O(n).

        :param data: the item to search
        :returns: the position of the item if it exists in the tree, else None
        """
        if self.is_empty():
            raise Empty("Tree is empty")

        current_node = self._root

        while current_node is not None:
            left_child = current_node.children[0]
            right_child = current_node.children[1]
            if data == current_node.data:
                break
            elif data > current_node.data:
                current_node = right_child
            else:
                current_node = left_child

        if current_node is None:
            return None
        else:
            return Tree._Position(self, current_node)
