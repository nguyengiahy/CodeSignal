import heapq
INF = int(1e9)

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
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
                path[neighbor.id] = u
                heapq.heappush(pq, Node(neighbor.id, dist[neighbor.id]))

def printPath(u):
    if path[u] == -1:
        print(u, end="->")
    else:
        printPath(path[u])
        if u == f:
            print(u)
        else:
            print(u, end="->")

if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n+5)]
    dist = [INF] * (n+5)
    path = [-1] * (n+5)
    for i in range(n):
        d = list(map(int, input().split()))
        for j in range(n):
            if d[j] > 0:
                graph[i].append(Node(j, d[j]))
    s, f = 0, 4
    Dijkstra(s)
    if dist[f] != -1:
        print(dist[f])
        printPath(f)


''' 
Test input:6
0 1 0 0 0 0
0 0 5 2 0 7
0 0 0 0 0 1
2 0 1 0 4 0
0 0 0 3 0 0 
0 0 0 0 1 0

Output: 6
0->1->3->2->5->4
'''