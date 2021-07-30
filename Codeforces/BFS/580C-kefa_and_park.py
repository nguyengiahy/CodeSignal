from queue import Queue
MAX = 100000 + 5
cat = [0] * MAX
graph = [[] for _ in range(MAX)]
visited = [False] * MAX

def BFS():
    q = Queue()
    q.put(1)
    visited[1] = True
    cat[1] = a[1]
    res = 0

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                if a[v]:
                    cat[v] = cat[u] + 1
                else:
                    cat[v] = 0
                if cat[v] <= m:
                    visited[v] = True
                    if len(graph[v]) == 1:
                        res += 1
                    else:
                        q.put(v)
    return res

n, m = map(int, input().split())
a = [None] + list(map(int, input().split()))

for i in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(BFS())