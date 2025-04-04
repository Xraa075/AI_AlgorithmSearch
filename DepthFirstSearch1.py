from queue import PriorityQueue

# Representasi graf dari gambar
graph_weighted = {
    'S': {'B': 2, 'A': 4},
    'B': {'S': 2, 'A': 1, 'C': 7},
    'A': {'S': 4, 'B': 1, 'D': 3},
    'C': {'B': 7, 'D': 2, 'Z': 2},
    'D': {'A': 3, 'C': 2, 'Z': 5},
    'Z': {'C': 2, 'D': 5}
}

def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    visited.add(start)
    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None

print("DFS Path:", dfs(graph_weighted, 'S', 'Z'))
