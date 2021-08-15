import heapq
INF = int(1e9)

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist < other.dist

def Dijkstra(s):
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

q = int(input())
case = 0
for _ in range(q):
    case += 1
    n, m, s, t = map(int, input().split())
    graph = [[] for _ in range(n)]
    dist = [INF] * n
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))
    Dijkstra(s)
    print("Case #" + str(case) + ": ", end="")
    print(dist[t] if dist[t] != INF else "unreachable")