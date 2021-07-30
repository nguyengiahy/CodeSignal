from queue import Queue
MAX = 1005
graph = [[] for _ in range(MAX)]
visited = [False for _ in range(MAX)]
distance = [0 for _ in range(MAX)]
Q = int(input())
V, E = None, None

def BFS(s):
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 6
                q.put(v)

    # Clear data for next test
    for i in range(1, V+1):
        graph[i].clear()
        visited[i] = False

for _ in range(Q):
    V, E = map(int, input().split())
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = int(input())
    # ----- BFS -----
    BFS(s)
    # ----- Print result -------
    for i in range(1, V+1):
        if i != s:
            if distance[i] == 0:
                print(-1, end=" ")
            else:
                print(distance[i], end=" ")
        # Clear data for next test
        distance[i] = 0
    print()