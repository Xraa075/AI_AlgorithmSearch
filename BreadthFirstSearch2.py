from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

graph_weighted = {
    'A': {'B': 3, 'C': 5},
    'B': {'A': 3, 'C': 6, 'D': 4},
    'C': {'A': 5, 'B': 6, 'E': 3},
    'D': {'B': 4, 'E': 5, 'F': 3},
    'E': {'C': 3, 'D': 5, 'G': 2},
    'F': {'D': 3, 'G': 6, 'Z': 2},
    'G': {'E': 2, 'F': 6, 'Z': 3},
    'Z': {'F': 2, 'G': 3}
}

print("BFS Path:", bfs(graph_weighted, 'A', 'Z'))
