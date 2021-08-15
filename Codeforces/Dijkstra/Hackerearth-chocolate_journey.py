from heapq import heappop, heappush
INF = int(1e9)

def Dijkstra(s, dist):
    dist[s] = 0
    pq = []
    heappush(pq, (0, s))

    while len(pq) > 0:
        w, u = heappop(pq)
        if w > dist[u]:
            continue
        for v, weight in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))

n, m, k, expire = map(int, input().split())
chocolate_cities = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
distS = [INF] * (n+1)
distT = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

s, t = map(int, input().split())

Dijkstra(s, distS)
Dijkstra(t, distT)

shortest_path = INF
for city in chocolate_cities:
    if distT[city] <= expire and distS[city] + distT[city] < shortest_path:
        shortest_path = distS[city] + distT[city]

print(shortest_path if shortest_path < INF else -1)