from enum import Enum
from typing import List
from binary_tree import BinaryTree


class BinaryExpressionTree(BinaryTree):
    """ A binary expression tree is a binary tree used to parse mathematical expressions. Operators are contained
    within the internal nodes of the tree, whereas the operands occupy the leaves. By using such a parse tree, complex
    mathematical expressions with numerous operators and operands can be easily evaluated, as the expression is divided
    into smaller parts made up of only two operands and a single operator.

    Instantiating a binary expression tree
        >>> tree = BinaryExpressionTree()

    Evaluate expressions, when tree parsing is based on infix notation
        >>> tree.evaluate("(2+2-23)", BinaryExpressionTree.Notation.Infix)
        -19.0
        >>> tree.evaluate("((434+42-2)*(43+4-2))", BinaryExpressionTree.Notation.Infix)
        21330.0

    Evaluate expressions, when tree parsing is based on prefix notation
        >>> tree.evaluate("(2+2-23)", BinaryExpressionTree.Notation.Prefix)
        -19.0
        >>> tree.evaluate("((434+42-2)*(43+4-2))", BinaryExpressionTree.Notation.Prefix)
        21330.0

    Evaluate expressions, when tree parsing is based on postfix notation
        >>> tree.evaluate("(2+2-23)", BinaryExpressionTree.Notation.Postfix)
        -19.0
        >>> tree.evaluate("((434+42-2)*(43+4-2))", BinaryExpressionTree.Notation.Postfix)
        21330.0
    """
    Notation = Enum("Notation", "Infix Prefix Postfix")

    def __init__(self):
        super().__init__()
        self.__current_node = None

    @staticmethod
    def __get_tokens(expression: str):
        tokens = []
        len_of_expression = len(expression)
        i = 0

        while i < len_of_expression:
            j = i
            token = ""
            operator = None

            while j < len_of_expression:
                token += expression[j]
                j += 1

                try:
                    _ = float(token)
                except ValueError:
                    if token[-1] == ".":
                        continue
                    elif token[-1] in "()+-*/":
                        operator = token[-1]
                        token = token[:-1]
                        break
                    else:
                        raise ValueError(f"'{token[-1]}' is not a valid operator or operand")

            if len(token) > 0:
                tokens.append(token)
            if operator is not None:
                tokens.append(operator)
            i = j

        return tokens

    @staticmethod
    def __infix_to_prefix(tokens: List[str]):
        operators = []
        operands = []
        prefix_tokens = []

        for token in tokens:
            if token in "(+-*/":
                operators.append(token)
            elif token == ")":
                if len(operands) > 0:
                    while operators[-1] != "(":
                        prefix_tokens.append(operators.pop())
                    _ = operators.pop()
                    prefix_tokens.extend(operands)
                    operands.clear()
                else:
                    while operators[-1] != "(":
                        prefix_tokens.insert(0, operators.pop())
                    _ = operators.pop()
            else:
                operands.append(token)

        prefix_tokens.extend(operands)

        return prefix_tokens

    @staticmethod
    def __infix_to_postfix(tokens: List[str]):
        operators = []
        postfix_tokens = []

        for token in tokens:
            if token in "(+-*/":
                operators.append(token)
            elif token == ")":
                while operators[-1] != "(":
                    postfix_tokens.append(operators.pop())
                _ = operators.pop()
            else:
                postfix_tokens.append(token)

        return postfix_tokens

    def __insert_infix(self, data):
        super().insert(data)

        if data not in "()+-*/":
            try:
                _ = float(data)
            except ValueError:
                raise ValueError(f"'{data}' is not a valid operator or operand")

        if self.is_empty():
            self._root = BinaryTree._Node(None, children=[None, None])
            self.__current_node = self._root

            self.__insert_infix(data)

        else:
            if data == "(":
                node = BinaryTree._Node(None, parent=self.__current_node, children=[None, None])
                self.__current_node.children[0] = node

                self.__current_node = node

            elif data == ")":
                self.__current_node = self.__current_node.parent

            elif data in "+-*/":
                if self.__current_node is None:
                    node = BinaryTree._Node(None, parent=self.__current_node, children=[self._root, None])
                    new_right_node = BinaryTree._Node(None, parent=node, children=[None, None])

                    node.children[1] = new_right_node
                    self._root.parent = node
                    self._root = node

                    node.data = data
                    self.__current_node = new_right_node

                elif self.__current_node.data is None:
                    node = BinaryTree._Node(None, parent=self.__current_node, children=[None, None])
                    self.__current_node.children[1] = node

                    self.__current_node.data = data
                    self.__current_node = node

                else:
                    parent = self.__current_node.parent

                    if parent is None or parent.data is not None:
                        node = BinaryTree._Node(None, parent=parent, children=[self.__current_node, None])
                        new_right_node = BinaryTree._Node(None, parent=node, children=[None, None])

                        self.__current_node.parent = node
                        node.children[1] = new_right_node

                        if parent is not None:
                            is_left_child = parent.children[0] == self.__current_node
                            if is_left_child:
                                parent.children[0] = node
                            else:
                                parent.children[1] = node
                        else:
                            self._root = node

                        node.data = data
                        self.__current_node = new_right_node

                    else:
                        node = BinaryTree._Node(None, parent=parent, children=[None, None])
                        parent.children[1] = node

                        parent.data = data
                        self.__current_node = node

            else:
                self.__current_node.data = data
                self.__current_node = self.__current_node.parent

    def __insert_prefix(self, data):
        super().insert(data)

        if data not in "()+-*/":
            try:
                _ = float(data)
            except ValueError:
                raise ValueError(f"'{data}' is not a valid operator or operand")

        if self.is_empty():
            self._root = BinaryTree._Node(data, children=[None, None])
            self.__current_node = self._root

        else:
            if self.__current_node.children[0] is None:
                node = BinaryTree._Node(data, parent=self.__current_node, children=[None, None])
                self.__current_node.children[0] = node
                if data in "+-*/":
                    self.__current_node = node
            elif self.__current_node.children[1] is None:
                node = BinaryTree._Node(data, parent=self.__current_node, children=[None, None])
                self.__current_node.children[1] = node
                if data in "+-*/":
                    self.__current_node = node
            else:
                while self.__current_node.children[1] is not None:
                    self.__current_node = self.__current_node.parent
                node = BinaryTree._Node(data, parent=self.__current_node, children=[None, None])
                self.__current_node.children[1] = node
                if data in "+-*/":
                    self.__current_node = node

    def __insert_postfix(self, data):
        super().insert(data)

        if data not in "()+-*/":
            try:
                _ = float(data)
            except ValueError:
                raise ValueError(f"'{data}' is not a valid operator or operand")

        if self.__current_node is None:
            self.__current_node = [BinaryTree._Node(data, children=[None, None])]
        elif data in "+-*/":
            right = self.__current_node.pop()
            left = self.__current_node.pop()
            self.__current_node.append(BinaryTree._Node(data, children=[left, right]))
        else:
            self.__current_node.append(BinaryTree._Node(data, children=[None, None]))

        if len(self.__current_node) == 1:
            self._root = self.__current_node[0]

    def __parse(self, expression: str, notation: Notation):
        def insert_helper(token_list, callback):
            for token in token_list:
                try:
                    callback(token)
                except AttributeError:
                    raise SyntaxError

        tokens = BinaryExpressionTree.__get_tokens(expression)

        if notation == BinaryExpressionTree.Notation.Infix:
            insert_helper(tokens, self.__insert_infix)
        elif notation == BinaryExpressionTree.Notation.Prefix:
            prefix_tokens = self.__infix_to_prefix(tokens)
            insert_helper(prefix_tokens, self.__insert_prefix)
        elif notation == BinaryExpressionTree.Notation.Postfix:
            postfix_tokens = self.__infix_to_postfix(tokens)
            insert_helper(postfix_tokens, self.__insert_postfix)

    def __refresh(self):
        self.__init__()

    def insert(self, data):
        """ Inserts a value into the tree. Operators and operands inserted need to follow the infix notation when using
        this method.

        :param data: item to be added to the tree
        """
        self.__insert_infix(data)

    def delete(self, position: BinaryTree._Position):
        if not position.is_owned_by(self):
            raise ValueError("Position doesn't belong to this tree")

        super().delete(position)

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
            is_left_child = None if parent is None else node_to_delete.data < parent.data

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
                    new_node = BinaryTree._Node(right_child.data, children=[current_node, right])

                    insert_node(new_node, is_left_child, parent)
                    if is_root:
                        self._root = new_node

                    delete_node(right_child, False)

        node = position.manipulate_node(self, "_validate_node")
        is_root_node = self.is_root(position)
        _ = position.manipulate_variables(self, "_invalidate_position")

        delete_node(node, is_root_node)

    def evaluate(self, expression: str, notation: Notation = Notation.Infix):
        """ Returns the solution to a mathematical expression

        :param expression: the expression to be solved
        :param notation: the notation to use when building the parse tree
        :returns: the solution to the passed expression
        """
        def evaluate_helper(node: BinaryTree._Node):
            try:
                if node.children == [None, None]:
                    return float(node.data)
            except AttributeError:
                raise SyntaxError

            left_result = evaluate_helper(node.children[0])
            right_result = evaluate_helper(node.children[1])
            operator = node.data

            if operator == "+":
                return left_result + right_result
            elif operator == "-":
                return left_result - right_result
            elif operator == "*":
                return left_result * right_result
            elif operator == "/":
                return left_result / right_result
            else:
                raise ValueError(f"'{operator}' is not a valid operator")

        self.__refresh()
        self.__parse(expression, notation)

        if self.is_empty():
            return 0.0
        else:
            return evaluate_helper(self._root)
