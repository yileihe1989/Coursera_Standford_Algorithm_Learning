"""
python implementation of topological sort
Rationale for this algorithm: every time after we finish a DFS, the unvisited points would only have two scenarios:
1) It is the above the all the visited points; 2) It does not have a directed path to visited points
"""

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        """
        :param vertices: number of vertices
        """
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        if u >= self.V or v >= self.V:
            raise ValueError("Invalid node number!")
        self.graph[u].append(v)

    def _dfs(self, node, visited, stack):
        """
        :param node: graph node dict
        :param visited: mutable variable. Hence can be modified in place
        :param stack: mutable variable. Hence can be modified in place
        :return: None
        """
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        stack.insert(0, node)

    def topological_sorting(self):
        visited = {i: False for i in range(self.V)}
        stack = []
        for node in range(self.V):
            if not visited[node]:
                self._dfs(node, visited, stack)
        return stack


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    print(g.topological_sorting())

    t = Graph(4)
    t.add_edge(0, 1)
    t.add_edge(0, 2)
    t.add_edge(2, 3)
    t.add_edge(1, 3)
    print(t.topological_sorting())

