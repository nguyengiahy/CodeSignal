def DFS(s):
    global leaf, max_dist
    stack = []
    stack.append(s)
    dist = [-1] * (V+1)
    dist[s] = 0

    while len(stack) > 0:
        u = stack.pop()
        for v, w in graph[u]:
            if dist[v] == -1:   # if v has not been visited
                dist[v] = dist[u] + w
                if dist[v] > max_dist:
                    leaf = v    # the furthest node from node s -> this node lies on tree diameter
                    max_dist = dist[v]
                stack.append(v)

t = int(input())
for _ in range(t):
    V = int(input())
    E = V - 1

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))

    leaf = 0
    max_dist = 0
    DFS(1)
    DFS(leaf)

    print(max_dist)