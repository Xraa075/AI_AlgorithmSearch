from queue import PriorityQueue

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
print("Best-First Search Path:", best_first_search(graph_weighted, 'A', 'Z', heuristic))
