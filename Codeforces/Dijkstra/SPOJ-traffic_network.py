import heapq
INF = int(1e9)

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s, dist, graph):
    dist[s] = 0
    pq = []
    heapq.heappush(pq, Node(s, 0))

    while len(pq) > 0:
        top = heapq.heappop(pq)
        u = top.id
        w = top.dist
        if w > dist[u]:
            continue
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                heapq.heappush(pq, Node(neighbor.id, dist[neighbor.id]))

t = int(input())
for _ in range(t):
    n, m, k, s, t = map(int, input().split())
    graphS = [[] for _ in range(n + 1)]
    graphT = [[] for _ in range(n + 1)]
    distS = [INF] * (n + 1)
    distT = [INF] * (n + 1)
    for _ in range(m):
        u, v, w = map(int, input().split())
        graphS[u].append(Node(v, w))
        graphT[v].append(Node(u, w))

    Dijkstra(s, distS, graphS)
    Dijkstra(t, distT, graphT)
    res = distS[t]
    for _ in range(k):
        u, v, w = map(int, input().split())
        res = min(res, distS[u] + w + distT[v])
        res = min(res, distS[v] + w + distT[u])
    print(res if res != INF else -1)