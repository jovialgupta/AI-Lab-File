def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node in visited:
        return

    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        dfs(graph, neighbour, visited)


graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [5],
    5: []
}

dfs(graph, 0)