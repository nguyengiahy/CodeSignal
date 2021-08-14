import heapq
INF = int(1e9)

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist < other.dist

def Dijkstra(s, f):
    dist = [INF] * (n + 1)
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

    return dist[f]

t = int(input())
for _ in range(t):
    n = int(input())
    cities = [0]
    graph = [[] for _ in range(n+1)]

    for i in range(n):
        city = input()
        cities.append(city)
        m = int(input())
        for _ in range(m):
            v, w = map(int, input().split())
            graph[i+1].append(Node(v, w))

    r = int(input())
    for _ in range(r):
        c1, c2 = input().split()
        s = cities.index(c1)
        f = cities.index(c2)
        print(Dijkstra(s, f))
    input()