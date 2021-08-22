INF = int(1e9)

def BellmanFord(s):
    dist[s] = 0
    for i in range(n-1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Find all vertices that are affected by negative cycles
    for i in range(n):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF

test  = int(input())
for tc in range(test):
    input()
    n = int(input())
    busyness = [-1] + list(map(int, input().split()))
    m = int(input())

    dist = [INF] * (n+1)
    graph = []
    for i in range(m):
        u, v = map(int, input().split())
        graph.append((u, v, (busyness[v] - busyness[u]) ** 3))

    BellmanFord(1)

    print("Case " + str(tc+1) + ":")
    q = int(input())
    for _ in range(q):
        t = int(input())
        print("?" if dist[t] < 3 or dist[t] == INF else dist[t])