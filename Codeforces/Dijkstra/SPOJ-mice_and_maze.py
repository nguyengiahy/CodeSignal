import heapq
INF = int(1e9)

N = int(input())
E = int(input())
T = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

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

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append(Node(u, w))     # Reverse the direction, because we will Dijkstra from destination

Dijkstra(E)

res = 0
for i in range(1, N+1):
    if dist[i] <= T:
        res += 1
print(res)