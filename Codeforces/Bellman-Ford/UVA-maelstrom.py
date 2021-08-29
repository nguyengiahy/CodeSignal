INF = int(1e9)

def BellmanFord(s):
    dist[s] = 0
    for i in range(n-1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

n = int(input())
dist = [INF] * (n+1)
graph = []

for i in range(2, n+1):
    line = input().split()
    for j in range(1, i):
        if line[j-1] != 'x':
            w = int(line[j-1])
            graph.append((i, j, w))
            graph.append((j, i, w))
m = len(graph)

BellmanFord(1)
res = 0
for i in range(1, n+1):
    res = max(res, dist[i])
print(res)