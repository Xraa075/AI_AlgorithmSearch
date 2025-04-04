def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {n: {m: float('inf') if m != n else 0 for m in nodes} for n in nodes}

    for u in graph:
        for v, weight in graph[u].items():
            dist[u][v] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

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

result = floyd_warshall(graph_weighted)
print("Floyd-Warshall Result:")
for i in result:
    print(i, result[i])
