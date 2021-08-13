from queue import Queue
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
INF = int(1e9)

def isValid(r, c):
    return r in range(R) and c in range(C)

def BFS(x, y):
    q = Queue()
    q.put((x, y))
    graph[x][y] = 1
    cost = [[INF] * C for _ in range(R)]
    cost[x][y] = 0

    while not q.empty():
        u = q.get()

        for i in range(4):
            r = u[0] + dr[i]
            c = u[1] + dc[i]
            if isValid(r,c) and graph[r][c] == 0:
                graph[r][c] = 1
                cost[r][c] = min(cost[r][c], cost[u[0]][u[1]] + 1)
                q.put((r, c))

    return cost[dx][dy]

while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break
    graph = [[0] * C for _ in range(R)]

    rows = int(input())
    for _ in range(rows):
        array = list(map(int, input().split()))
        i = array[0]
        n = array[1]
        for j in range(n):
            graph[i][array[j+2]] = 1

    sx, sy = map(int, input().split())
    dx, dy = map(int, input().split())
    print(BFS(sx, sy))