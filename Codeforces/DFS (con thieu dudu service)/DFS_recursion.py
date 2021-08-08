MAX = 1000 + 5
graph = [[] for _ in range(MAX)]
visited = [False for _ in range(MAX)]
path = [-1 for _ in range(MAX)]

def printPath(u):
    if path[u] == -1:
        print(u, end="->")
    else:
        printPath(path[u])
        if u == f:
            print(u)
        else:
            print(u, end="->")

def DFS(s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            path[v] = s
            DFS(v)

if __name__ == "__main__":
    n, m = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s, f = map(int, input().split())
    DFS(s)
    if visited[f]:
        printPath(f)
    else:
        print("There is no path from", s, "to", f)