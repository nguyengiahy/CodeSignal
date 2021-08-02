from queue import Queue
T = int(input())
MAX = 100002
graph = [[] for _ in range(MAX)]
visited = [False for _ in range(MAX)]

def DFS(s):
    stack = []
    visited[s] = True
    stack.append(s)

    while len(stack) > 0:
        u = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

for _ in range(T):
    N = int(input())
    E = int(input())
    for i in range(N):
        graph[i].clear()
        visited[i] = False

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    res = 0
    for i in range(N):
        if not visited[i]:
            res += 1
            DFS(i)
    print(res)