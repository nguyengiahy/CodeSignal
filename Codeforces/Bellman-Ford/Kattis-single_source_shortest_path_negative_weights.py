INF = int(1e9)

def BellmanFord(s):
    dist[s] = 0
    for i in range(n-1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for i in range(n):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF

while True:
    n, m, q, s = map(int, input().split())
    if n == 0 and m == 0 and q == 0 and s == 0: break

    graph = []
    dist = [INF] * n
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))

    BellmanFord(s)
    for _ in range(q):
        x = int(input())
        if dist[x] == INF:
            print("Impossible")
        elif dist[x] == -INF:
            print("-Infinity")
        else:
            print(dist[x])
    print()