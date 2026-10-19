from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [5],
    5: []
}

bfs(graph, 0)