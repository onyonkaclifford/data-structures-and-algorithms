from binary_search_tree import BinarySearchTree
from tree import Tree


class AVLTree(BinarySearchTree):
    """An AVL tree is a binary search tree that is balanced. Whenever an item is inserted or deleted, the tree
    rebalances itself. This ensures an a worst case search time of O(logn).

    Instantiating an AVL tree
        >>> tree = AVLTree()

    Inserting an item to the tree
        >>> tree.insert(5, 500)
        >>> tree.insert(4, 400)
        >>> tree.insert(6, 600)
        >>> tree.insert(10, 10000)

    Check if a tree is empty
        >>> tree.is_empty()
        False
        >>> AVLTree().is_empty()
        True

    Get root position
        >>> root = tree.get_root()

    Get item corresponding to a certain position
        >>> root.get_data()
        (5, 500)

    Check if a position is owned by some tree
        >>> root.is_owned_by(tree)
        True
        >>> root.is_owned_by(AVLTree())
        False

    Get children of some position
        >>> children = tree.get_children(root)
        >>> [i.get_data() for i in children]
        [(4, 400), (6, 600)]

    Get left child of some position
        >>> left_child = tree.get_left_child(root)
        >>> left_child.get_data()
        (4, 400)

    Get right child of some position
        >>> right_child = tree.get_right_child(root)
        >>> right_child.get_data()
        (6, 600)

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
        (5, 500)
        >>> tree.get_parent(root) is None
        True

    Get siblings of some position
        >>> siblings = tree.get_siblings(left_child)
        >>> [i.get_data() for i in siblings]
        [(6, 600)]

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
        >>> len(AVLTree())
        0

    Get string reresentation of tree
        >>> tree
        5(4, 6)
        >>> str(tree)
        '5(4, 6)'

    Get tree iterable
        >>> tree_iterable = iter(tree)
        >>> next(tree_iterable).get_data()
        (5, 500)

    Get next item of tree iterator
        >>> next(tree).get_data()
        (4, 400)
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def __rotate(node_to_move, root_node, parent, clockwise):
        node_to_move.parent = parent
        if parent is not None:
            is_left_child = root_node.key < parent.key
            if is_left_child:
                parent.children[0] = node_to_move
            else:
                parent.children[1] = node_to_move
        if clockwise:
            node_to_move.children[1] = root_node
        else:
            node_to_move.children[0] = root_node
        root_node.parent = node_to_move

    def __get_balance(self, root_node):
        if root_node is None:
            return 0
        left_height = (
            0
            if root_node.children[0] is None
            else self.get_height_of_node(Tree._Position(self, root_node.children[0]))
        )
        right_height = (
            0
            if root_node.children[1] is None
            else self.get_height_of_node(Tree._Position(self, root_node.children[1]))
        )
        return left_height - right_height

    def __balance_tree(self):
        def balance_tree(root_node):
            parent = root_node.parent
            left_child = root_node.children[0]
            right_child = root_node.children[1]

            if left_child is not None:
                balance_tree(left_child)

            if right_child is not None:
                balance_tree(right_child)

            balance = self.__get_balance(root_node)

            if abs(balance <= 1):
                return root_node

            if balance > 0:
                current = root_node.children[0]
                right = current.children[1]
                if right is None:
                    AVLTree.__rotate(current, root_node, parent, clockwise=True)
                    return current
                else:
                    new_node = Tree._Node(
                        right.key, right.value, parent=parent, children=[current, None]
                    )
                    AVLTree.__rotate(new_node, root_node, parent, clockwise=True)
                    current.parent = new_node
                    self.delete(Tree._Position(self, right))
                    return new_node
            else:
                current = root_node.children[1]
                left = current.children[0]
                if left is None:
                    AVLTree.__rotate(current, root_node, parent, clockwise=False)
                    return current
                else:
                    new_node = Tree._Node(
                        left.key, left.value, parent=parent, children=[None, current]
                    )
                    AVLTree.__rotate(new_node, root_node, parent, clockwise=False)
                    current.parent = new_node
                    self.delete(Tree._Position(self, left))
                    return new_node

        self.__root = balance_tree(self._root)

    def delete(self, position: Tree._Position):
        super().delete(position)
        self.__balance_tree()

    def insert(self, key, value):
        super().insert(key, value)
        self.__balance_tree()
