from graph import Graph


class AdjacencyMatrixGraph(Graph):
    """ An adjacency matrix graph is a graph implemented based on a 2-dimensional array-like structure with the vertices
    of the graph aligned to both axes. The intersection of both axes marks that the corresponding vertices are connected
    with an edge, with the value contained at the intersection denoting the weight of the edge. An empty intersection
    denotes that the corresponding vertices are not connected.

    Instantiating an adjacency matrix graph
        >>> directed_graph = AdjacencyMatrixGraph(directed=True)
        >>> undirected_graph = AdjacencyMatrixGraph(directed=False)

    Check if a graph is directed
        >>> directed_graph.is_directed()
        True
        >>> undirected_graph.is_directed()
        False

    Add a vertex to a graph
        >>> directed_graph.add_vertex(1, 1000)
        >>> directed_graph.add_vertex(2, 2000)
        >>> directed_graph.add_vertex(3, 3000)
        >>> directed_graph.add_vertex(4, 4000)
        >>> directed_graph.add_vertex(5, 5000)

        >>> undirected_graph.add_vertex(1, 1000)
        >>> undirected_graph.add_vertex(2, 2000)
        >>> undirected_graph.add_vertex(3, 3000)
        >>> undirected_graph.add_vertex(4, 4000)
        >>> undirected_graph.add_vertex(5, 5000)

    Add an edge to a graph
        >>> directed_graph.add_edge(1, 2, 100)
        >>> directed_graph.add_edge(1, 3, 200)
        >>> directed_graph.add_edge(1, 4, 300)
        >>> directed_graph.add_edge(2, 3, 400)
        >>> directed_graph.add_edge(2, 5, 500)
        >>> directed_graph.add_edge(3, 5, 600)
        >>> directed_graph.add_edge(4, 5, 700)

        >>> undirected_graph.add_edge(1, 2, 100)
        >>> undirected_graph.add_edge(1, 3, 200)
        >>> undirected_graph.add_edge(1, 4, 300)
        >>> undirected_graph.add_edge(2, 3, 400)
        >>> undirected_graph.add_edge(2, 5, 500)
        >>> undirected_graph.add_edge(3, 5, 600)
        >>> undirected_graph.add_edge(4, 5, 700)

    Get keys of all the vertices in a graph
        >>> directed_graph.get_vertices()
        [1, 2, 3, 4, 5]
        >>> undirected_graph.get_vertices()
        [1, 2, 3, 4, 5]

    Get all the edges in a graph
        >>> directed_graph.get_edges()
        [(1, 2, 100), (1, 3, 200), (1, 4, 300), (2, 3, 400), (2, 5, 500), (3, 5, 600), (4, 5, 700)]
        >>> undirected_graph.get_edges()
        [(1, 2, 100), (1, 3, 200), (1, 4, 300), (2, 1, 100), (2, 3, 400), (2, 5, 500), (3, 1, 200), (3, 2, 400), \
(3, 5, 600), (4, 1, 300), (4, 5, 700), (5, 2, 500), (5, 3, 600), (5, 4, 700)]

    Check if a pair of vertices form an edge
        >>> directed_graph.is_edge(1, 2)
        True
        >>> directed_graph.is_edge(2, 1)
        False
        >>> directed_graph.is_edge(1, 5)
        False

        >>> undirected_graph.is_edge(1, 2)
        True
        >>> undirected_graph.is_edge(2, 1)
        True
        >>> undirected_graph.is_edge(1, 5)
        False

    Get incoming edges of a vertex
        >>> directed_graph.get_incoming_edges(3)
        [(1, 3, 200), (2, 3, 400)]

        >>> undirected_graph.get_incoming_edges(3)
        [(1, 3, 200), (2, 3, 400), (5, 3, 600)]

    Get outgoing edges of a vertex
        >>> directed_graph.get_outgoing_edges(3)
        [(3, 5, 600)]

        >>> undirected_graph.get_outgoing_edges(3)
        [(3, 1, 200), (3, 2, 400), (3, 5, 600)]

    Get the weight of some edge
        >>> directed_graph.get_edge_weight(1, 2)
        100

        >>> undirected_graph.get_edge_weight(1, 2)
        100

    Get adjacent vertices relative to some vertex
        >>> directed_graph.get_adjacent_vertices(2)
        [(1, 100), (3, 400), (5, 500)]

        >>> undirected_graph.get_adjacent_vertices(2)
        [(1, 100), (3, 400), (5, 500)]

    Get adjacent incoming vertices relative to some vertex
        >>> directed_graph.get_incoming_adjacent_vertices(2)
        [(1, 100)]

        >>> undirected_graph.get_incoming_adjacent_vertices(2)
        [(1, 100), (3, 400), (5, 500)]

    Get adjacent outgoing vertices relative to some vertex
        >>> directed_graph.get_outgoing_adjacent_vertices(2)
        [(3, 400), (5, 500)]

        >>> undirected_graph.get_outgoing_adjacent_vertices(2)
        [(1, 100), (3, 400), (5, 500)]

    Get value stored in a vertex
        >>> directed_graph.get_vertex_value(1)
        1000

        >>> undirected_graph.get_vertex_value(1)
        1000

    String representation of a graph
        >>> str(directed_graph)
        '[-, 100, 200, 300, -]\\n[-, -, 400, -, 500]\\n[-, -, -, -, 600]\\n[-, -, -, -, 700]\\n[-, -, -, -, -]'

        >>> str(undirected_graph).strip()
        '[-, 100, 200, 300, -]\\n[-, -, 400, -, 500]\\n[-, -, -, -, 600]\\n[-, -, -, -, 700]\\n[-, -, -, -, -]'

    Check if a vertex corresponding to some key is contained in the graph
        >>> 1 in directed_graph
        True
        >>> 100 in directed_graph
        False

        >>> 1 in undirected_graph
        True
        >>> 100 in undirected_graph
        False

    Depth-first traversal of a graph
        >>> [i for i in directed_graph.depth_first_traversal(1)]
        [(1, 1), (2, 2), (3, 3), (5, 4), (4, 8)]

        >>> [i for i in undirected_graph.depth_first_traversal(1)]
        [(1, 1), (2, 2), (3, 3), (5, 4), (4, 8)]

    Breadth-first traversal of a graph
        >>> [i for i in directed_graph.breadth_first_traversal(1)]
        [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

        >>> [i for i in undirected_graph.breadth_first_traversal(1)]
        [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    Delete an edge
        >>> directed_graph.remove_edge(1, 2)

        >>> undirected_graph.remove_edge(1, 2)

    Delete a vertex
        >>> directed_graph.remove_vertex(1)

        >>> undirected_graph.remove_vertex(1)
    """

    class _Empty:
        def __repr__(self):
            return "-"

    def __init__(self, directed):
        super().__init__(directed)
        self.__adjacency_matrix = []

    def __repr__(self):
        s = ""
        for i in self.__adjacency_matrix:
            s += f"{str(i)}\n"

        if len(self.__adjacency_matrix) > 0:
            s = s[:-1]

        return s

    def _get_next_vertices(self, key):
        super()._get_next_vertices(key)

        idx = self._keys.index(key)
        row = self.__adjacency_matrix[idx]

        return [
            (self._keys[i], weight) for i, weight in enumerate(row)
            if not isinstance(weight, AdjacencyMatrixGraph._Empty)
        ]

    def add_vertex(self, key, value=None):
        super().add_vertex(key, value)
        self.__adjacency_matrix.append([AdjacencyMatrixGraph._Empty() for _ in range(len(self._keys) - 1)])

        for row in self.__adjacency_matrix:
            row.append(AdjacencyMatrixGraph._Empty())

    def remove_vertex(self, key):
        idx = None
        if key in self:
            idx = self._keys.index(key)

        super().remove_vertex(key)
        del self.__adjacency_matrix[idx]

        for i in range(len(self.__adjacency_matrix)):
            del self.__adjacency_matrix[i][idx]

    def add_edge(self, key1, key2, weight=None):
        super().add_edge(key1, key2, weight)

        idx1 = self._keys.index(key1)
        idx2 = self._keys.index(key2)

        self.__adjacency_matrix[idx1][idx2] = weight

    def remove_edge(self, key1, key2):
        super().remove_edge(key1, key2)

        for i in self.get_adjacent_vertices(key1):
            if key2 == i[0]:
                idx1 = self._keys.index(key1)
                idx2 = self._keys.index(key2)
                self.__adjacency_matrix[idx1][idx2] = AdjacencyMatrixGraph._Empty()
                return

        if not self.is_directed():
            for i in self.get_adjacent_vertices(key2):
                if key1 == i[0]:
                    idx1 = self._keys.index(key1)
                    idx2 = self._keys.index(key2)
                    self.__adjacency_matrix[idx2][idx1] = AdjacencyMatrixGraph._Empty()
                    return

        raise ValueError(f"Edge ({key1}, {key2}) is absent from the graph")

    def get_edges(self):
        return super().get_edges()

    def get_adjacent_vertices(self, key):
        super().get_adjacent_vertices(key)

        idx = self._keys.index(key)
        vertices = []

        for i, row in enumerate(self.__adjacency_matrix):
            if i != idx:
                for j, weight in enumerate(row):
                    if j == idx and not isinstance(weight, AdjacencyMatrixGraph._Empty):
                        vertices.append((self._keys[i], weight))
            else:
                vertices.extend([
                    (self._keys[j], weight) for j, weight in enumerate(row)
                    if not isinstance(weight, AdjacencyMatrixGraph._Empty)
                ])

        return vertices

    def get_incoming_adjacent_vertices(self, key):
        super().get_incoming_adjacent_vertices(key)

        idx = self._keys.index(key)
        vertices = []

        for i, row in enumerate(self.__adjacency_matrix):
            if i != idx:
                for j, weight in enumerate(row):
                    if j == idx and not isinstance(weight, AdjacencyMatrixGraph._Empty):
                        vertices.append((self._keys[i], weight))
            else:
                if not self.is_directed():
                    vertices.extend([
                        (self._keys[j], weight) for j, weight in enumerate(row)
                        if not isinstance(weight, AdjacencyMatrixGraph._Empty)
                    ])

        return vertices

    def get_outgoing_adjacent_vertices(self, key):
        super().get_outgoing_adjacent_vertices(key)

        idx = self._keys.index(key)
        vertices = []

        for i, row in enumerate(self.__adjacency_matrix):
            if i != idx:
                if not self.is_directed():
                    for j, weight in enumerate(row):
                        if j == idx and not isinstance(weight, AdjacencyMatrixGraph._Empty):
                            vertices.append((self._keys[i], weight))
            else:
                vertices.extend([
                    (self._keys[j], weight) for j, weight in enumerate(row)
                    if not isinstance(weight, AdjacencyMatrixGraph._Empty)
                ])

        return vertices

    def get_edge_weight(self, key1, key2):
        return super().get_edge_weight(key1, key2)

    def get_outgoing_edges(self, key):
        return super().get_outgoing_edges(key)

    def get_incoming_edges(self, key):
        return super().get_incoming_edges(key)

    def is_edge(self, key1, key2):
        return super().is_edge(key1, key2)

    def depth_first_traversal(self, key):
        yield from super().depth_first_traversal(key)

    def breadth_first_traversal(self, key):
        yield from super().breadth_first_traversal(key)
