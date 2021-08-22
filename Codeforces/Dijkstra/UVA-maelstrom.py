import heapq
INF = int(1e9)

def Dijkstra(s):
    dist[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))

    while len(pq) > 0:
        w, u = heapq.heappop(pq)
        if w > dist[u]:
            continue
        for v, weight in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heapq.heappush(pq, (dist[v], v))

n = int(input())
dist = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(2, n+1):
    line = input().split()
    for j in range(1, i):
        if line[j-1] != 'x':
            w = int(line[j-1])
            graph[i].append((j, w))
            graph[j].append((i, w))

Dijkstra(1)
res = 0
for i in range(1, n+1):
    res = max(res, dist[i])
print(res)