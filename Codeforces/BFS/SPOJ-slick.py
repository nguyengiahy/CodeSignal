from queue import Queue
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def isValid(r, c):
    return r in range(N) and c in range(M)

def BFS(x, y):
    q = Queue()
    q.put((x,y))
    visited[x][y] = True
    area = 1

    while not q.empty():
        u = q.get()

        for i in range(4):
            r = u[0] + dr[i]
            c = u[1] + dc[i]
            if isValid(r,c) and slick[r][c] and not visited[r][c]:
                area += 1
                visited[r][c] = True
                q.put((r,c))

    return area

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0: break

    visited = [[False] * M for _ in range(N)]
    area = [0] * (N*M + 5)
    slick = [None] * N
    count = 0
    for i in range(N):
        slick[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and slick[i][j]:
                x = BFS(i,j)
                count += 1
                area[x] += 1
    print(count)
    for i in range(len(area)):
        if area[i]:
            print(i, area[i])
