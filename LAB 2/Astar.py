import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], g

        if g != cost[node]:
            continue

        for neighbour, weight in graph[node]:
            new_cost = g + weight

            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                parent[neighbour] = node
                heapq.heappush(
                    pq,
                    (new_cost + heuristic[neighbour],
                     new_cost, neighbour)
                )

    return None, float("inf")


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

path, cost = astar(graph, heuristic, 'A', 'D')

print("Path:", path)
print("Cost:", cost)