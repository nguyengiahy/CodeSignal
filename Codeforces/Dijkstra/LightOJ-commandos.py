import heapq
INF = int(1e9)

def Dijkstra(s, dist):
    dist[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))

    while len(pq) > 0:
        w, u = heapq.heappop(pq)
        if w > dist[u]:
            continue
        for neighbor in graph[u]:
            if w + 1 < dist[neighbor]:
                dist[neighbor] = w + 1
                heapq.heappush(pq, (dist[neighbor], neighbor))

q = int(input())
for case in range(q):
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n)]
    distS = [INF] * n
    distT = [INF] * n
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s, t = list(map(int, input().split()))

    Dijkstra(s, distS)
    Dijkstra(t, distT)

    res = 0
    for i in range(n):
        res = max(res, distS[i] + distT[i])

    print("Case " + str(case + 1) + ":", res)