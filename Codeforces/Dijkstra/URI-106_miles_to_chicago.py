import heapq
INF = float(1e9)

def Dijkstra(s):
    dist[s] = 1.0
    pq = []
    heapq.heappush(pq, (dist[s], s))

    while len(pq) > 0:
        w, u = heapq.heappop(pq)
        if w > dist[u]:
            continue
        for v, weight in graph[u]:
            if w * weight > dist[v]:
                dist[v] = w * weight
                heapq.heappush(pq, (dist[v], v))

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    n, m = arr[0], arr[1]

    graph = [[] for _ in range(n+1)]
    dist = [-INF] * (n+1)
    for _ in range(m):
        u, v, p = list(map(int, input().split()))
        graph[u].append((v, p/100.0))
        graph[v].append((u, p/100.0))

    Dijkstra(1)
    print("%.6f" %(dist[n] * 100), "percent")