INF = int(1e9)

def BellmanFord(s):
    dist[s] = 100
    for i in range(n-1):
        for j in range(m):
            u, v = graph[j]
            if dist[u] > 0 and dist[u] + energy[v] > dist[v]:
                dist[v] = dist[u] + energy[v]

    for i in range(n):
        for j in range(m):
            u, v = graph[j]
            if dist[u] > 0 and dist[u] + energy[v] > dist[v]:
                dist[v] = INF

while True:
    n = int(input())
    if n == -1: break

    energy = [0]
    dist = [-INF] * (n+1)
    graph = []
    for i in range(n):
        array = list(map(int, input().split()))
        energy.append(array[0])
        if array[1] > 0:
            for x in array[2:]:
                graph.append((i+1, x))
    m = len(graph)

    BellmanFord(1)
    print("winnable" if dist[n] > 0 else "hopeless")