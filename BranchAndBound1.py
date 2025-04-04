from queue import PriorityQueue

graph_weighted = {
    'S': {'B': 2, 'A': 4},
    'B': {'S': 2, 'A': 1, 'C': 7},
    'A': {'S': 4, 'B': 1, 'D': 3},
    'C': {'B': 7, 'D': 2, 'Z': 2},
    'D': {'A': 3, 'C': 2, 'Z': 5},
    'Z': {'C': 2, 'D': 5}
}

def branch_and_bound(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = set()
    
    while not pq.empty():
        cost, node, path = pq.get()
        if node == goal:
            return path
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                pq.put((cost + weight, neighbor, path + [neighbor]))
    return None

print("Branch and Bound Path:", branch_and_bound(graph_weighted, 'S', 'Z'))