import heapq
INF = int(1e9)
class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s):
    pq = []
    heapq.heappush(pq, Node(s, 0))
    dist[s] = 0

    while len(pq) > 0:
        top = heapq.heappop(pq)
        u, w = top.id, top.dist
        for v in graph[u]:
            if w + v.dist < dist[v.id]:
                dist[v.id] = w + v.dist
                path[v.id] = u
                heapq.heappush(pq, Node(v.id, dist[v.id]))

if __name__ == "__main__":
    n = int(input())
    s, f = 0, 4
    graph = [[] for _ in range(n+5)]
    dist = [INF] * (n+5)
    path = [-1] * (n+5)
    for i in range(n):
        d = list(map(int, input().split()))
        for j in range(n):
            if d[j] > 0:
                graph[i].append(Node(j,d[j]))

    Dijkstra(s)
    ans = dist[f]
    print(ans)


''' 
Test input:
6
0 1 0 0 0 0
0 0 5 2 0 7
0 0 0 0 0 1
2 0 1 0 4 0
0 0 0 3 0 0 
0 0 0 0 1 0
Output: 6
'''