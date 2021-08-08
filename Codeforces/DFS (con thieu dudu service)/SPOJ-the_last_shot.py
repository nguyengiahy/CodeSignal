N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

def DFS(s):
    visited = [False] * (N + 1)
    stack = []
    stack.append(s)
    visited[s] = True
    max_bombs = 1

    while len(stack) > 0:
        u = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                max_bombs += 1
                stack.append(v)
    return max_bombs

res = 1
for i in range(1, N+1):
    res = max(res, DFS(i))

print(res)