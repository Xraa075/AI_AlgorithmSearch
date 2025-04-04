from queue import PriorityQueue

graph_weighted = {
    'S': {'B': 2, 'A': 4},
    'B': {'S': 2, 'A': 1, 'C': 7},
    'A': {'S': 4, 'B': 1, 'D': 3},
    'C': {'B': 7, 'D': 2, 'Z': 2},
    'D': {'A': 3, 'C': 2, 'Z': 5},
    'Z': {'C': 2, 'D': 5}
}

def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {n: {m: float('inf') if m != n else 0 for m in nodes} for n in nodes}
    
    for u in graph:
        for v, weight in graph[u].items():
            dist[u][v] = weight
    
    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

print("Floyd-Warshall Result:")
distance_matrix = floyd_warshall(graph_weighted)
for row in distance_matrix:
    print(row, distance_matrix[row])