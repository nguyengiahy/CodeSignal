from queue import Queue
MAX = 100
graph = [[] for _ in range(MAX)]
visited = [False for _ in range(MAX)]
path = [-1 for _ in range(MAX)]

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
                path[v] = u

def printPath(u):
    if path[u] == -1:
        print(u, end="->")
    else:
        printPath(path[u])
        if u != f:
            print(u, end="->")
        else:
            print(u)

if __name__ == "__main__":
    V, E = map(int, input().split())
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s, f = map(int, input().split())
    BFS(s)
    if visited[f]:
        printPath(f)
    else:
        print("There is no path from", s, "to", f)