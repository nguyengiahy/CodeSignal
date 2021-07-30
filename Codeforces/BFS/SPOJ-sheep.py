from queue import Queue
MAX = 250 + 5
backyard = [[None] for _ in range(MAX)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

N, M = map(int, input().split())
for i in range(N):
    backyard[i] = list(input())

def isInside(r, c):
    return r in range(N) and c in range(M)

def BFS(i, j):
    sheep = wolves = 0
    flag = False
    if backyard[i][j] == 'k':
        sheep += 1
    if backyard[i][j] == 'v':
        wolves += 1
    backyard[i][j] = '#'

    q = Queue()
    q.put((i,j))

    while not q.empty():
        u = q.get()
        for i in range(4):
            r = u[0] + dr[i]
            c = u[1] + dc[i]
            if not isInside(r,c):
                flag = True
            if isInside(r,c) and backyard[r][c] != '#':
                if backyard[r][c] == 'k':
                    sheep += 1
                if backyard[r][c] == 'v':
                    wolves += 1
                backyard[r][c] = '#'
                q.put((r,c))

    if flag:
        return (sheep, wolves)
    else:
        if wolves >= sheep:
            return (0, wolves)
        else:
            return (sheep, 0)

res = [0, 0]
for i in range(N):
    for j in range(M):
        if backyard[i][j] != '#':
            (sheep, wolves) = BFS(i,j)
            res[0] += sheep
            res[1] += wolves

print(res[0], res[1])