from queue import Queue
MAX = 20 + 5
visited = [[False] * MAX for _ in range(MAX)]
place = [[None] for _ in range(MAX)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
T = int(input())

def isValid(r, c):
    return r in range(H) and c in range(W)

def BFS(sr, sc):
    q = Queue()
    q.put((sr, sc))
    visited[sr][sc] = True
    res = 1

    while not q.empty():
        u = q.get()
        for i in range(4):
            r = u[0] + dr[i]
            c = u[1] + dc[i]

            if isValid(r, c) and place[r][c] == '.' and not visited[r][c]:
                res += 1
                visited[r][c] = True
                q.put((r,c))
    return res

for order in range(T):
    W, H = map(int, input().split())
    sr = sc = -1
    for i in range(H):
        place[i] = list(input())
        for j in range(W):
            visited[i][j] = False
            if place[i][j] == '@':
                sr = i
                sc = j
    print("Case " + str(order + 1) + ":", BFS(sr, sc))