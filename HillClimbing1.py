from queue import PriorityQueue

graph_weighted = {
    'S': {'B': 2, 'A': 4},
    'B': {'S': 2, 'A': 1, 'C': 7},
    'A': {'S': 4, 'B': 1, 'D': 3},
    'C': {'B': 7, 'D': 2, 'Z': 2},
    'D': {'A': 3, 'C': 2, 'Z': 5},
    'Z': {'C': 2, 'D': 5}
}

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

heuristic = {'S': 6, 'B': 4, 'A': 5, 'C': 2, 'D': 3, 'Z': 0}
print("Hill Climbing Path:", hill_climbing(graph_weighted, 'S', 'Z', heuristic))