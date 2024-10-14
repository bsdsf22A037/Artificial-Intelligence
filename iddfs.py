# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        # Number of vertices
        self.V = vertices
        # Initialize the adjacency list for each vertex with an empty list
        self.graph = [[] for _ in range(vertices)]

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        # Since it's a directed graph, add v to the adjacency list of u
        self.graph[u].append(v)

    # A utility function to perform Depth-Limited Search (DLS)
    def DLS(self, src, target, maxDepth):
        # If the current node is the target, return True
        if src == target:
            return True

        # If maxDepth is 0, we've reached the limit and return False
        if maxDepth <= 0:
            return False

        # Recur for all the vertices adjacent to the current node
        for i in self.graph[src]:
            if self.DLS(i, target, maxDepth - 1):
                return True

        # If target is not reachable within maxDepth, return False
        return False

    # IDDFS algorithm that uses DLS() to find if the target is reachable
    def IDDFS(self, src, target, maxDepth):
        # Loop through all depths from 0 to maxDepth - 1
        for i in range(maxDepth):
            # Use DLS for each depth and return True if target is found
            if self.DLS(src, target, i):
                return True
        # If target is not found in any depth, return False
        return False

# Create a graph and add edges
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

# Define source, target, and max depth for the search
target = 6
maxDepth = 3
src = 0

if g.IDDFS(src, target, maxDepth):
    print("Target is reachable from source within max depth")
else:
    print("Target is NOT reachable from source within max depth")
