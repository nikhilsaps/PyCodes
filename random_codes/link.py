class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1][vertex2] = weight
        self.graph[vertex2][vertex1] = weight  # For an undirected graph

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")


# Example usage:
g = Graph()
g.add_edge("A", "B", 2)
g.add_edge("A", "C", 1)
g.add_edge("B", "C", 3)
g.add_edge("B", "D", 4)

g.display()