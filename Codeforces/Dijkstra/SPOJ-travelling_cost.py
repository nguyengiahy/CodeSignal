import heapq
INF = int(1e9)
MAX = 500 + 5

graph = [[] for _ in range(MAX)]
dist = [INF] * (MAX)

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

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

n = int(input())
for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))

s = int(input())
Dijkstra(s)
m = int(input())
for _ in range(m):
    f = int(input())
    print(dist[f] if dist[f] != INF else "NO PATH")