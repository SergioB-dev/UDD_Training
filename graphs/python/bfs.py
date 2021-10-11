

adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['B', 'C', 'D', 'F'],
    'F': ['D', 'E']
}

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            deVertex = queue.pop(0)
            print(deVertex)

            for adjV in self.gdict[deVertex]:
                if adjV not in visited:
                    visited.append(adjV)
                    queue.append(adjV)


g1 = Graph(adj_list)
g1.bfs('A')

# Prints A -> B -> C -> D -> E -> F
