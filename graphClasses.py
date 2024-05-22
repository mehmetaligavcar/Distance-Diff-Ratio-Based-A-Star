class Vertex:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.id} ({self.x}, {self.y})'


class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __str__(self):
        return f'{self.vertex1.id} -> {self.vertex2.id} ({self.weight})'


class Graph:
    def __init__(self, vertexes, edges):
        self.elements = {}
        for vertex in vertexes:
            edges_from = []
            for edge in edges:
                if edge.vertex1 == vertex:
                    edges_from.append(edge)
                    other_edge = Edge(edge.vertex2, edge.vertex1, edge.weight)
                    if edge.vertex2 in self.elements.keys():
                        self.elements[edge.vertex2].append(other_edge)
                    else:
                        self.elements[edge.vertex2] = [other_edge]
            if vertex in self.elements.keys():
                self.elements[vertex].extend(edges_from)
            else:
                self.elements[vertex] = edges_from

    def get(self, vertex):
        for element in self.elements:
            if element.id == vertex.id:
                return self.elements[element]
