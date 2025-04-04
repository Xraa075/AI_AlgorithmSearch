from queue import PriorityQueue

def branch_and_bound(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    
    while not pq.empty():
        cost, node, path = pq.get()
        if node == goal:
            return path, cost
        for neighbor, weight in graph[node].items():
            if neighbor not in path:
                pq.put((cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

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

path, cost = branch_and_bound(graph_weighted, 'A', 'Z')
print("Branch and Bound Path:", path, "with cost:", cost)
