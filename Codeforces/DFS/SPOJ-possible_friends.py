def DFS(i):
    visited = [False] * V
    visited[i] = True
    depth = [0] * V		
    friends = 0

    stack = []
    stack.append(i)

    while len(stack) > 0:
        u = stack.pop()
        if depth[u] == 2:
            friends += 1
            continue
        for v in edges[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                stack.append(v)
    return friends

t = int(input())
for _ in range(t):
    line = input()
    V = len(line)

    graph = []
    edges = [[] for _ in range(V)]

    for i in range(V):
        if i == 0:
            graph.append(line)
        else:
            graph.append(input())
        for j in range(V):
            if graph[i][j] == 'Y':
                edges[i].append(j)

    max_friends = idx = 0
    for i in range(V):
        friends = DFS(i)
        if friends > max_friends:
            max_friends = friends
            idx = i

    print(idx, max_friends)