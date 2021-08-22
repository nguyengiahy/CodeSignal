from queue import Queue
INF = int(1e9)

def hasPathBFS(s, f):
    q = Queue()
    q.put(s)
    visited = [False] * (n+1)
    visited[s] = True

    while not q.empty():
        u = q.get()
        for source, target in graph:
            if source == u and not visited[target]:
                if target == f:
                    return True
                visited[target] = True
                q.put(target)

    return False

def BellmanFord(s):
    dist[s] = 100
    for i in range(n-1):
        for j in range(m):
            u, v = graph[j]
            if dist[u] > 0 and dist[u] + energy[v] > dist[v]:
                dist[v] = dist[u] + energy[v]

    for i in range(m):
        u, v = graph[i]
        if dist[u] > 0 and dist[u] + energy[v] > dist[v] and hasPathBFS(u, n):
            dist[n] = INF
            break

while True:
    n = int(input())
    if n == -1: break

    energy = [0]
    dist = [-INF] * (n+1)
    graph = []
    for i in range(n):
        array = list(map(int, input().split()))
        energy.append(array[0])
        if array[1] > 0:
            for x in array[2:]:
                graph.append((i+1, x))
    m = len(graph)

    BellmanFord(1)
    print("winnable" if dist[n] > 0 else "hopeless")