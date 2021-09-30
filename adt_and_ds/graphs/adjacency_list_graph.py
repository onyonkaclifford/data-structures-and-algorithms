from graph import Graph


class AdjacencyListGraph(Graph):
    """ An adjacency list graph is a graph implemented based on a mapping of each vertex to a list of all vertices that
    are adjacent to it.

    Instantiating an adjacency list graph
        >>> directed_graph = AdjacencyListGraph(directed=True)
        >>> undirected_graph = AdjacencyListGraph(directed=False)

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
        '{\\n\\t1: [(2, 100), (3, 200), (4, 300)]\\n\\t2: [(3, 400), (5, 500)]\\n\\t3: [(5, 600)]\\n\\t\
4: [(5, 700)]\\n\\t5: []\\n}'

        >>> str(undirected_graph).strip()
        '{\\n\\t1: [(2, 100), (3, 200), (4, 300)]\\n\\t2: [(3, 400), (5, 500)]\\n\\t3: [(5, 600)]\\n\\t\
4: [(5, 700)]\\n\\t5: []\\n}'

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

    def __init__(self, directed):
        super().__init__(directed)
        self.__adjacency_list = {}

    def __repr__(self):
        s = "{\n"
        for k, v in self.__adjacency_list.items():
            s += f"\t{k}: {v}\n"
        s += "}"

        return s

    def _get_next_vertices(self, key):
        super()._get_next_vertices(key)
        return self.__adjacency_list[key]

    def add_vertex(self, key, value=None):
        super().add_vertex(key, value)
        self.__adjacency_list[key] = []

    def remove_vertex(self, key):
        super().remove_vertex(key)
        del self.__adjacency_list[key]

    def add_edge(self, key1, key2, weight=None):
        super().add_edge(key1, key2, weight)
        self.__adjacency_list[key1].append((key2, weight))

    def remove_edge(self, key1, key2):
        super().remove_edge(key1, key2)

        for i in self.get_adjacent_vertices(key1):
            if key2 == i[0]:
                self.__adjacency_list[key1].remove(i)
                return

        if not self.is_directed():
            for i in self.get_adjacent_vertices(key2):
                if key1 == i[0]:
                    self.__adjacency_list[key2].remove(i)
                    return

        raise ValueError(f"Edge ({key1}, {key2}) is absent from the graph")

    def get_edges(self):
        return super().get_edges()

    def get_adjacent_vertices(self, key):
        super().get_adjacent_vertices(key)

        vertices = []

        for k, adjacent in self.__adjacency_list.items():
            if k != key:
                for i in adjacent:
                    if i[0] == key:
                        vertices.append((k, i[1]))
            else:
                vertices.extend(adjacent)

        return vertices

    def get_incoming_adjacent_vertices(self, key):
        super().get_incoming_adjacent_vertices(key)

        vertices = []

        for k, adjacent in self.__adjacency_list.items():
            if k != key:
                for i in adjacent:
                    if i[0] == key:
                        vertices.append((k, i[1]))
            else:
                if not self.is_directed():
                    vertices.extend(adjacent)

        return vertices

    def get_outgoing_adjacent_vertices(self, key):
        super().get_outgoing_adjacent_vertices(key)

        vertices = []

        for k, adjacent in self.__adjacency_list.items():
            if k != key:
                if not self.is_directed():
                    for i in adjacent:
                        if i[0] == key:
                            vertices.append((k, i[1]))
            else:
                vertices.extend(adjacent)

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
