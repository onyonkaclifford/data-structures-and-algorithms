from abc import ABC, abstractmethod


class Graph(ABC):
    """ A graph is a set of vertices and the edges that connect these vertices together in pairs. The graph abstract
    data type can be implemented based on various structures, but the most common are:

    1. adjacency matrix
    2. adjacency list

    Graph vocabularies include, but are not limited to:

    1. Directed graph: a graph whose edges have an order, such that one of the vertices in each edge precedes the other.
        It's also called a digraph.
    2. Undirected graph: a graph whose edges have no order, such that each vertex has no precedence over any other
        vertex.
    3. Multi-graph: a graph that contains at least one pair of vertices joined by multiple edges.
    4. Complete graph: a graph whose vertices are each connected to every other vertex within the graph.
    5. Degree of a vertex: the number of edges connected to the vertex.
    6. Weight of an edge: the cost of traversing the edge.
    7. Path: a complete route from some vertex to some other vertex within the graph.
    8. Circuit: a path that begins and ends at the same vertex without traversing any edge more than once.
    """

    class _Vertex:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __repr__(self):
            return str(self.key)

    def __init__(self, directed):
        self._directed = directed
        self._keys = []
        self._vertices = []

    @abstractmethod
    def __repr__(self):
        """ Returns a string representation of the graph

        :returns: the string representation of the graph
        """
        raise NotImplementedError

    def __contains__(self, key):
        """ Checks if a graph contains a vertex with the passed key

        :param key: the key to check
        :returns: True if the key is contained in some vertex of the graph, else False
        """
        return key in self._keys

    @abstractmethod
    def _get_next_vertices(self, key):
        """ Returns the next vertices after some vertex when traversing the graph in some specific direction

        :param key: the key from where the traversing is originating
        :returns: next vertices after some vertex when traversing the graph in some specific direction
        """
        if key not in self:
            raise KeyError(f"{key} is absent from the graph")

    def is_directed(self):
        """ Checks if the graph is directed

        :returns: True if the graph is directed, else False
        """
        return self._directed

    def get_vertices(self):
        """ Returns a list of the keys of all vertices contained within the graph

        :returns: a list of all the vertices' keys
        """
        return self._keys

    def get_vertex_value(self, key):
        """ Returns the value stored in the vertex corresponding to the passed key

        :param key: the key whose corresponding vertex's value is being sought
        :returns: the value associated to vertex of the passed key
        """
        if key not in self:
            raise KeyError(f"{key} is absent from the graph")

        idx = self._keys.index(key)
        return self._vertices[idx].value

    @abstractmethod
    def add_vertex(self, key, value=None):
        """ Add a new vertex to the graph

        :param key: the key to associate to the new vertex
        :param value: the value to be stored in the new vertex
        """
        if key in self:
            raise KeyError(f"{key} already exists in the graph")

        self._keys.append(key)
        self._vertices.append(Graph._Vertex(key, value))

    @abstractmethod
    def remove_vertex(self, key):
        """ Delete the vertex associated to the passed key

        :param key: the key whose vertex id to be deleted
        """
        if key not in self:
            raise KeyError(f"{key} is absent from the graph")

        idx = self._keys.index(key)

        del self._keys[idx]
        del self._vertices[idx]

    @abstractmethod
    def add_edge(self, key1, key2, weight=None):
        """ Connect the vertices associated to the passed keys with a new edge

        :param key1: the key associated to the first vertex in the pair
        :param key2: the key associated to the second vertex in the pair
        :param weight: the cost of traversing the newly formed edge
        """
        if key1 not in self:
            raise KeyError(f"{key1} is absent from the graph")
        if key2 not in self:
            raise KeyError(f"{key2} is absent from the graph")

    @abstractmethod
    def remove_edge(self, key1, key2):
        """ Delete the edge connecting the vertices associated with the passed keys

        :param key1: the key associated with the first vertex of the edge pair
        :param key2: the key associated with the second vertex of the edge pair
        """
        if key1 not in self:
            raise KeyError(f"{key1} is absent from the graph")
        if key2 not in self:
            raise KeyError(f"{key2} is absent from the graph")

    @abstractmethod
    def get_edges(self):
        """ Returns a list of all the edges in the graph

        :returns: a list of all the edges
        """
        edges = []

        for i in self.get_vertices():
            for j in self.get_outgoing_adjacent_vertices(i):
                edges.append((i, j[0], j[1]))

        return edges

    @abstractmethod
    def get_adjacent_vertices(self, key):
        """ Returns a list of keys of all the vertices connected to the vertex associated with the passed key

        :param key: the key whose vertex all adjacent vertices' keys are being sought
        :returns: a list of vertex keys
        """
        if key not in self:
            raise KeyError(f"{key} is absent from the graph")

    @abstractmethod
    def get_incoming_adjacent_vertices(self, key):
        """ Returns a list of keys of all the vertices incoming to the vertex associated with the passed key

        :param key: the key whose vertex all incoming vertices' keys are being sought
        :returns: a list of vertex keys
        """
        if key not in self:
            raise KeyError(f"{key} is absent from the graph")

    @abstractmethod
    def get_outgoing_adjacent_vertices(self, key):
        """ Returns a list of keys of all the vertices outgoing from the vertex associated with the passed key

        :param key: the key whose vertex all outgoing vertices' keys are being sought
        :returns: a list of vertex keys
        """
        if key not in self:
            raise KeyError(f"{key} is absent from the graph")

    @abstractmethod
    def get_edge_weight(self, key1, key2):
        """ Returns the weight associated with the edge connecting the vertices associated with the vertices of the
        passed keys

        :param key1: the key of the first vertex in the edge pair
        :param key2: the key of the second vertex in the edge pair
        :returns: weight of the edge
        """
        if key1 not in self:
            raise KeyError(f"{key1} is absent from the graph")
        if key2 not in self:
            raise KeyError(f"{key2} is absent from the graph")

        for i in self.get_adjacent_vertices(key1):
            if key2 == i[0]:
                return i[1]

        if not self.is_directed():
            for i in self.get_adjacent_vertices(key2):
                if key1 == i[0]:
                    return i[1]

        raise ValueError(f"Edge ({key1}, {key2}) is absent from the graph")

    @abstractmethod
    def get_outgoing_edges(self, key):
        """ Returns a list of outgoing edges corresponding to the vertex associated with the passed key

        :param key: the key whose vertex a list of outgoing edges is being sought
        :returns: a list of edges
        """
        if key not in self:
            raise KeyError(f"{key} is absent from the graph")

        return [(key, *i) for i in self.get_outgoing_adjacent_vertices(key)]

    @abstractmethod
    def get_incoming_edges(self, key):
        """ Returns a list of incoming edges corresponding to the vertex associated with the passed key

        :param key: the key whose vertex a list of incoming edges is being sought
        :returns: a list of edges
        """
        if key not in self:
            raise KeyError(f"{key} is absent from the graph")

        return [(i[0], key, i[1]) for i in self.get_incoming_adjacent_vertices(key)]

    @abstractmethod
    def is_edge(self, key1, key2):
        """ Checks if a pair of vertices form an edge

        :param key1: the key of the first vertex in the edge pair
        :param key2: the key of the second vertex in the edge pair
        :returns: True if the passed pair form an edge, else False
        """
        if key1 not in self:
            raise KeyError(f"{key1} is absent from the graph")
        if key2 not in self:
            raise KeyError(f"{key2} is absent from the graph")

        for i in self.get_outgoing_adjacent_vertices(key1):
            if key2 == i[0]:
                return True

        return False

    @abstractmethod
    def depth_first_traversal(self, key):
        """ Returns a generator that yields keys of vertices of the graph when traversed depth first from some vertex

        :param key: the key where the traversal begins from
        :returns: a generator of vertex keys
        """
        visited = {"__steps": 0}

        def helper(vertex_key):
            visited["__steps"] += 1
            visited[vertex_key] = {"first_visit": visited["__steps"]}

            yield vertex_key, visited["__steps"]

            for k, _ in self._get_next_vertices(vertex_key):
                if k not in visited.keys():
                    yield from helper(k)

            visited["__steps"] += 1
            visited[vertex_key] = {"last_visit": visited["__steps"]}

        yield from helper(key)

    @abstractmethod
    def breadth_first_traversal(self, key):
        """ Returns a generator that yields keys of vertices of the graph when traversed breadth first from some vertex

        :param key: the key where the traversal begins from
        :returns: a generator of vertex keys
        """
        visited = {"__steps": 1, key: {"visit": 1}}
        helper_queue = [key]

        while len(helper_queue) > 0:
            current_key = helper_queue.pop(0)

            yield current_key, visited[current_key]["visit"]

            for k, _ in self._get_next_vertices(current_key):
                if k not in visited.keys():
                    visited["__steps"] += 1
                    visited[k] = {"visit": visited["__steps"]}
                    helper_queue.append(k)
