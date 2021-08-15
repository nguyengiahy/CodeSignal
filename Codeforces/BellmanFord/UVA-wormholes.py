INF = int(1e9)

def BellmanFord(s):
    dist[s] = 0
    for i in range(n-1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for i in range(m):
        u, v, w = graph[i]
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    graph = []
    dist = [INF] * n
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))
    res = BellmanFord(0)
    print("possible" if not res else "not possible")