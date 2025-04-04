def hill_climbing(graph, start, goal, heuristic):
    current = start
    path = [current]
    
    while current != goal:
        neighbors = sorted(graph[current], key=lambda x: heuristic[x])
        if heuristic[neighbors[0]] >= heuristic[current]:
            return None  # Terjebak di local optimum
        current = neighbors[0]
        path.append(current)
    return path

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

heuristic = {'A': 10, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 3, 'G': 4, 'Z': 0}
print("Hill Climbing Path:", hill_climbing(graph_weighted, 'A', 'Z', heuristic))
