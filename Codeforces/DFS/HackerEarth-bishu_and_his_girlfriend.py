from queue import Queue
n = int(input())
MAX = 1002
graph = [[] for _ in range(MAX)]
visited = [False for _ in range(MAX)]
distance = [0 for _ in range(MAX)]
destination = []

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

Q = int(input())

for _ in range(Q):
    destination.append(int(input()))

destination.sort()

def BFS(s):
    q = Queue()
    q.put(s)
    visited[s] = True
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                distance[v] = distance[u] + 1

BFS(1)
min_path = 10000
res = 0
for i in range(len(destination)):
    if distance[destination[i]] < min_path:
        min_path = distance[destination[i]]
        res = destination[i]

print(res)