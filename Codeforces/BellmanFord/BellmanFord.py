INF = int(1e9)
MAX = 100

graph = []
dist = [INF] * MAX
path = [-1] * MAX

def BellmanFord(s):
    dist[s] = 0
    for i in range(1, n):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(m):
        u, v, w = graph[i]
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True

def printPath(x):
    if path[x] == -1:
        print(x, end="->")
    else:
        printPath(path[x])
        if x == t:
            print(x)
        else:
            print(x, end="->")

if __name__ == "__main__":
    n, m = map(int, input().split())
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))
    s, t = map(int, input().split())
    res = BellmanFord(s)
    if not res:
        print("Graph contains negative weight cycle")
    else:
        print(dist[t])
        printPath(t)

'''Example test
input:
6 10 
0 1 1
1 2 5
1 3 -2
1 5 7
2 5 -1
3 0 2
3 2 -1
3 4 4
4 3 3
5 4 1
0 4
output:
-2
0->1->3->2->5->4