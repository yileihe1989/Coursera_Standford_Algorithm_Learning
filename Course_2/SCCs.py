"""
Python Implementation of Kosaraju’s Algorithm to find Strong Connected Component
"""


def dfs_r_node(graph, node, visited, stack):
    """
    dfs graph and create a stack-order node list
    """
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor] and neighbor != node:
            dfs_r_node(graph, neighbor, visited, stack)
    stack.insert(0, node)


def r_graph(graph):
    """
    reverse graph
    """
    reversed_graph = {}
    for node in graph.keys():
        for neighbor in graph[node]:
            if neighbor not in reversed_graph:
                reversed_graph[neighbor] = []
            reversed_graph[neighbor].append(node)
    return reversed_graph


def dfs_scc(graph, node, visited, scc):
    visited[node] = True
    if node in graph:
        for neighbor in graph[node]:
            if not visited[neighbor] and neighbor != node:
                dfs_scc(graph, neighbor, visited, scc)
    scc.append(node)


if __name__ == "__main__":
    graph = {
        "1": ["3"],
        "3": ["4", "5", "6"],
        "5": [],
        "4": [],
        "6": ["3", "7"],
        "7": ["8"],
        "8": ["6"]
    }

    # graph = {
    #     "1": ["0"],
    #     "2": ["3"],
    #     "0": ["0", "2", "9"],
    #     "3": ["1"],
    #     "9": ["5"],
    #     "5": ["7", "4", "10"],
    #     "7": ["5", "9"],
    #     "4": [],
    #     "10": ["5"]
    # }

    node_set = set(graph.keys())
    for i, j in graph.items():
        node_set |= set(j)

    visited = {i: False for i in node_set}
    nodes_stack = []
    for node in graph.keys():
        if not visited[node]:
            dfs_r_node(graph, node, visited, nodes_stack)

    reversed_graph = r_graph(graph)

    scc_list = []
    visited = {i: False for i in node_set}
    for node in nodes_stack:
        print(node)
        if not visited[node]:
            scc = []
            dfs_scc(reversed_graph, node, visited, scc)
            scc_list.append(scc)
    print(scc_list)
