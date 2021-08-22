INF = float(1e9)

def BellmanFord(s):
    dist[s] = 1.0
    for i in range(n-1):
        for j in range(2*m):
            u, v, p = graph[j]
            if dist[u] > 0 and dist[u] * p > dist[v]:
                dist[v] = dist[u] * p

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    n, m = arr[0], arr[1]

    graph = []
    dist = [-1.0] * (n+1)
    for _ in range(m):
        u, v, p = list(map(int, input().split()))
        graph.append((u, v, p/100.0))
        graph.append((v, u, p/100.0))

    BellmanFord(1)
    print("%.6f" %(dist[n] * 100), "percent")