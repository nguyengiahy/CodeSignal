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

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    s, t = map(int, input().split())

    graph = [[] for _ in range(n)]
    graphS = [[] for _ in range(n)]
    graphT = [[] for _ in range(n)]
    distS = [INF] * n
    distT = [INF] * n
    dist = [INF] * n

    for _ in range(m):
        u, v, w = map(int, input().split())
        graphS[u].append(Node(v, w))
        graphT[v].append(Node(u, w))

    Dijkstra(s, distS, graphS)
    Dijkstra(t, distT, graphT)
    shortest_path = distS[t]

    for u in range(n):
        for neighbor in graphS[u]:
            v = neighbor.id
            w = neighbor.dist
            if distS[u] + w + distT[v] != shortest_path:    # this edge does not belong to shortest path => add it in the new graph
                graph[u].append(Node(v, w))

    Dijkstra(s, dist, graph)
    print(dist[t] if dist[t] != INF else -1)