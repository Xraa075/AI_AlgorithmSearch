from queue import PriorityQueue

graph_weighted = {
    'S': {'B': 2, 'A': 4},
    'B': {'S': 2, 'A': 1, 'C': 7},
    'A': {'S': 4, 'B': 1, 'D': 3},
    'C': {'B': 7, 'D': 2, 'Z': 2},
    'D': {'A': 3, 'C': 2, 'Z': 5},
    'Z': {'C': 2, 'D': 5}
}

def best_first_search(graph, start, goal, heuristic):
    pq = PriorityQueue()
    pq.put((heuristic[start], start, [start]))
    visited = set()
    
    while not pq.empty():
        _, node, path = pq.get()
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor, path + [neighbor]))
    return None

heuristic = {'S': 6, 'B': 4, 'A': 5, 'C': 2, 'D': 3, 'Z': 0}
print("Best-First Search Path:", best_first_search(graph_weighted, 'S', 'Z', heuristic))