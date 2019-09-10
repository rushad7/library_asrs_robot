from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return list(path)


graph = Graph([(1, 2, 1), (1, 11, 0.5), (2, 3, 1), (2, 12, 0.5), (3, 4, 1), (3, 13, 0.5), (4, 5, 1), (4, 14, 0.5), (5, 6, 1), (5, 15, 0.5), (6, 7, 1), (6, 16, 0.5), (7, 8, 1), (7, 17, 0.5), (8, 9, 1), (8, 18, 0.5), (9, 10, 1), (9, 19, 0.5), (10, 20, 0.5), (11, 12, 1), (11, 21, 0.5), (12, 13, 1), (12, 22, 0.5), (13, 14, 1), (13, 23, 0.5), (14, 15, 1), (14, 24, 0.5), (15, 16, 1), (15, 25, 0.5), (16, 17, 1), (16, 26, 0.5), (17, 18, 1), (17, 27, 0.5), (18, 19, 1), (18, 28, 0.5), (19, 20, 1), (19, 29, 0.5), (20, 30, 0.5), (21, 22, 1), (21, 31, 0.5), (22, 23, 1), (22, 32, 0.5), (23, 24, 1), (23, 33, 0.5), (24, 25, 1), (24, 34, 0.5), (25, 26, 1), (25, 35, 0.5), (26, 27, 1), (26, 36, 0.5), (27, 28, 1), (27, 37, 0.5), (28, 29, 1), (28, 38, 0.5), (29, 30, 1), (29, 39, 0.5), (30, 40, 0.5), (31, 32, 1), (31, 41, 0.5), (32, 33, 1), (32, 42, 0.5), (33, 34, 1), (33, 43, 0.5), (34, 35, 1), (34, 44, 0.5), (35, 36, 1), (35, 45, 0.5), (36, 37, 1), (36, 46, 0.5), (37, 38, 1), (37, 47, 0.5), (38, 39, 1), (38, 48, 0.5), (39, 40, 1), (39, 49, 0.5), (40, 50, 0.5), (41, 42, 1), (41, 51, 0.5), (42, 43, 1), (42, 52, 0.5), (43, 44, 1), (43, 53, 0.5), (44, 45, 1), (44, 54, 0.5), (45, 46, 1), (45, 55, 0.5), (46, 47, 1), (46, 56, 0.5), (47, 48, 1), (47, 57, 0.5), (48, 49, 1), (48, 58, 0.5), (49, 50, 1), (49, 59, 0.5), (50, 60, 0.5), (51, 52, 1), (51, 61, 0.5), (52, 53, 1), (52, 62, 0.5), (53, 54, 1), (53, 63, 0.5), (54, 55, 1), (54, 64, 0.5), (55, 56, 1), (55, 65, 0.5), (56, 57, 1), (56, 66, 0.5), (57, 58, 1), (57, 67, 0.5), (58, 59, 1), (58, 68, 0.5), (59, 60, 1), (59, 69, 0.5), (60, 70, 0.5), (61, 62, 1), (61, 71, 0.5), (62, 63, 1), (62, 72, 0.5), (63, 64, 1), (63, 73, 0.5), (64, 65, 1), (64, 74, 0.5), (65, 66, 1), (65, 75, 0.5), (66, 67, 1), (66, 76, 0.5), (67, 68, 1), (67, 77, 0.5), (68, 69, 1), (68, 78, 0.5), (69, 70, 1), (69, 79, 0.5), (70, 80, 0.5), (71, 72, 1), (71, 81, 0.5), (72, 73, 1), (72, 82, 0.5), (73, 74, 1), (73, 83, 0.5), (74, 75, 1), (74, 84, 0.5), (75, 76, 1), (75, 85, 0.5), (76, 77, 1), (76, 86, 0.5), (77, 78, 1), (77, 87, 0.5), (78, 79, 1), (78, 88, 0.5), (79, 80, 1), (79, 89, 0.5), (80, 90, 0.5), (81, 82, 1), (81, 91, 0.5), (82, 83, 1), (82, 92, 0.5), (83, 84, 1), (83, 93, 0.5), (84, 85, 1), (84, 94, 0.5), (85, 86, 1), (85, 95, 0.5), (86, 87, 1), (86, 96, 0.5), (87, 88, 1), (87, 97, 0.5), (88, 89, 1), (88, 98, 0.5), (89, 90, 1), (89, 99, 0.5), (90, 100, 0.5), (91, 92, 1), (92, 93, 1), (93, 94, 1), (94, 95, 1), (95, 96, 1), (96, 97, 1), (97, 98, 1), (98, 99, 1), (99, 100, 1)])

print(graph.dijkstra(4, 56))
