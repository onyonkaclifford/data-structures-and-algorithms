from typing import Callable, List, Union


class Trie:
    """ A trie is a search tree whose nodes each contain a single string character, and have zero or many children. When
    traversed depth-first, if a complete word is formed, the node at which the path terminates at may be mapped to a
    value. The root node is unique from the rest of the nodes, in that it doesn't carry any key, or may carry a special
    key such as an empty string. Tries may be used to predict auto-complete text, where given a certain prefix, all
    possible combinations of words to complete the prefix can be generated. They may also be used as map structures such
    as associative arrays, which when passed a string key, return the corresponding value.

    Instantiating a trie object
        >>> a_trie = Trie()

    Inseerting a key and its corresponding value to the trie
        >>> a_trie.insert("Hello", 1)
        >>> a_trie.insert("World", 2)

    Checking if a trie is empty
        >>> a_trie.is_empty()
        False
        >>> Trie().is_empty()
        True

    Get length of some trie
        >>> len(a_trie)
        10
        >>> len(Trie())
        0

    Get the string representation of some trie
        >>> a_trie
        (H(e(l(l(o)))), W(o(r(l(d)))))
        >>> str(a_trie)
        '(H(e(l(l(o)))), W(o(r(l(d)))))'

    Get value associated to some key
        >>> a_trie["Hello"]
        1
        >>> a_trie.get_value("World")
        2
        >>> a_trie["Hello, world"]
        Traceback (most recent call last):
        ...
        KeyError: 'key not present in trie'

    Replace value associated to some key
        >>> a_trie["Hello"] = 100
        >>> a_trie.replace("World", 200)
        >>> a_trie["Hello, world"] = 300
        Traceback (most recent call last):
        ...
        KeyError: 'key not present in trie'

    Find all strings with some certain prefix
        >>> a_trie.prefix_search("He")
        ['Hello']
        >>> a_trie.prefix_search("qwerty")
        []

    Delete a key, and thus its corresponding value too, from the trie
        >>> del a_trie["Hello"]
        >>> a_trie.delete("World")
        >>> del a_trie["Hello, world"]
        Traceback (most recent call last):
        ...
        KeyError: 'key not present in trie'

    """

    class _Node:
        def __init__(self, key=None, value=None, children: Union[List, None] = None, end_of_string=False):
            self.key = key
            self.value = value
            self.children = children if children is not None else []
            self.end_of_string = end_of_string

    def __init__(self):
        self.__root = Trie._Node()
        self.__length = 0

    def __len__(self):
        """ Returns total number of nodes in trie. Time complexity: O(1).

        :return: total number of nodes in trie
        """
        return self.__length

    def __repr__(self):
        """ Returns a string representation of the trie. Time complexity: O(n).

        :return: the string representation of the trie
        """
        def helper(current_node: Trie._Node):
            children = current_node.children
            num_of_children = len(children)
            last_child_idx = num_of_children - 1

            if current_node.key is not None:
                data_dict["string_data"] += f"{current_node.key}"

            for i, j in enumerate(children):
                data_dict["string_data"] += "(" if i == 0 else ", "
                helper(j)
                data_dict["string_data"] += ")" if i == last_child_idx else ""

        if self.is_empty():
            return ""

        data_dict = {"string_data": ""}
        helper(self.__root)
        return data_dict["string_data"]

    def __getitem__(self, key: str):
        """ Alias of get_value
        """
        return self.get_value(key)

    def __setitem__(self, key: str, value):
        """ Alias of replace
        """
        self.replace(key, value)

    def __delitem__(self, key: str):
        """ Alias of delete
        """
        self.delete(key)

    def __get_node_for_key(self, key: str, not_found_callback: Callable, create_node=False):
        current_node = self.__root
        path = [current_node]

        for k in key:
            to_break = False
            for node in current_node.children:
                if node.key == k:
                    current_node = node
                    path.append(node)
                    to_break = True
                    break
            if not to_break:
                not_found_callback()
                if create_node:
                    new_node = Trie._Node(k)
                    current_node.children.append(new_node)
                    current_node = new_node
                    self.__length += 1

        return current_node, path

    def is_empty(self):
        """ Returns True if trie is empty, else False. Time complexity: O(1).

        :returns: True if trie is empty, else False
        """
        return self.__length == 0

    def insert(self, key: str, value=None):
        """ Inserts a key and its corresponding value into the trie

        :param key: key to insert
        :param value: value corresponding to the key
        """
        def not_found_callable():
            pass

        current_node, _ = self.__get_node_for_key(key, not_found_callable, create_node=True)
        current_node.value = value
        current_node.end_of_string = True

    def delete(self, key: str):
        """ Deletes a key and its corresponding value from the trie

        :param key: key to delete
        """
        def not_found_callable():
            raise KeyError("key not present in trie")

        current_node, path = self.__get_node_for_key(key, not_found_callable)
        end_of_string_occurrences = 0

        while len(path) > 1:
            node = path.pop()
            previous_node = path[-1]

            if node.end_of_string:
                if end_of_string_occurrences > 0:
                    break

                end_of_string_occurrences += 1
                node.value = None
                node.end_of_string = False

            if len(node.children) > 0:
                break
            else:
                previous_node.children.remove(node)
                self.__length -= 1

    def get_value(self, key: str):
        """ Returns the value associated with a certain key

        :param key: key whose value is being sought
        :returns: value corresponding to the passed key
        """
        def not_found_callable():
            raise KeyError("key not present in trie")

        current_node, _ = self.__get_node_for_key(key, not_found_callable)

        return current_node.value

    def replace(self, key: str, value):
        """ Replaces the value of a key with the new passed value

        :param key: key whose value is being replaced
        :param value: new value that's to replace current value of the passed key
        """
        def not_found_callable():
            raise KeyError("key not present in trie")

        current_node, _ = self.__get_node_for_key(key, not_found_callable)
        current_node.value = value

    def prefix_search(self, prefix: str):
        """ Returns all the combinations of words that can be formed from the passed prefix, as per to the trie

        :param prefix: first part of the words being sought
        :returns: all the combinations of words that can be formed from the passed prefix
        """
        def not_found_callable():
            raise KeyError("key not present in trie")

        def get_strings_helper(root_node: Trie._Node, starting_with: str):
            children = root_node.children

            if root_node.end_of_string:
                yield starting_with

            for child in children:
                for string_data in get_strings_helper(child, starting_with + child.key):
                    yield string_data

        try:
            current_node, _ = self.__get_node_for_key(prefix, not_found_callable)
        except KeyError:
            return []

        return [i for i in get_strings_helper(current_node, prefix)]
