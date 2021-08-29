INF = int(1e9)

def PrintPath(s, f):
    if s == f:
        print(s, end=' ')
        return
    if dist[s][f] == INF:
        print('No path', end='')
        return
    PrintPath(s, path[s][f])
    print(f, end=' ')
# ------------------------------------
def PrintSolution():
    for i in range(V):
        for j in range(V):
            if i != j:
                print("{} -> {}: ".format(i, j), end='')
                PrintPath(i, j)
                print()

                if dist[i][j] != INF:
                    print('Total cost: {}'.format(dist[i][j]))
# ------------------------------------
def FloydWarshall():
    for k in range(V):
        for i in range(V):
            if dist[i][k] == INF:
                continue
            for j in range(V):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

    for i in range(V):
        if dist[i][i] < 0:
            return False

    return True
# ------------------------------------
if __name__ == "__main__":
    V = int(input())

    graph = [[0 for _ in range(V)] for _ in range(V)]
    dist = [[INF for _ in range(V)] for _ in range(V)]
    path = [[-1 for _ in range(V)] for _ in range(V)]

    for i in range(V):
        line = list(map(int, input().split()))
        for j in range(V):
            graph[i][j] = INF if i != j and line[j] == 0 else line[j]
            dist[i][j] = graph[i][j]
            if i != j and graph[i][j] != INF:
                path[i][j] = i

    if FloydWarshall():
        PrintSolution()
    else:
        print("Graph contains negative weight cycle")



'''
6
0 1 0 0 0 0
0 0 5 -2 0 7
0 0 0 0 0 -1
2 0 -1 0 4 0
0 0 0 3 0 0
0 0 0 0 1 0
'''