INF = int(1e9)

def FloydWarshall():
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if i != j and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

def printResult():
    idx, friends = 0, 0

    for i in range(V):
        count = 0
        for j in range(V):
            if dist[i][j] == 2:
                count += 1
        if count > friends:
            idx = i
            friends = count

    print(idx, friends)

t = int(input())
for _ in range(t):
    line = list(input())
    V = len(line)

    graph = []
    dist = [[INF for _ in range(V)] for _ in range(V)]

    for i in range(V):
        if i == 0:
            graph.append(line)
        else:
            graph.append(list(input()))

        for j in range(V):
            if graph[i][j] == 'Y':
                dist[i][j] = 1

    FloydWarshall()
    printResult()