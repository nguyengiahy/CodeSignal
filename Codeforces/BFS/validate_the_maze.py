from queue import Queue
MAX = 21
maze = [None] * MAX
visited = [[False] * MAX for _ in range(MAX)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def isValid(x, y):
    return x in range(n) and y in range(m)

def BFS(s, f):
    q = Queue()
    q.put(s)
    visited[s[0]][s[1]] = True
    while not q.empty():
        u = q.get()

        if u[0] == f[0] and u[1] == f[1]: return True

        for i in range(4):
            r = u[0] + dr[i]
            c = u[1] + dc[i]

            if isValid(r,c) and maze[r][c] == '.' and not visited[r][c]:
                q.put((r,c))
                visited[r][c] = True
    return False

Q = int(input())
for _ in range(Q):
    n, m = map(int, input().split())
    for i in range(n):
        maze[i] = input()

    entrance = []
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            if maze[i][j] == '.' and (i == 0 or j == 0 or i == n-1 or j == m-1):
                entrance.append((i,j))

    if len(entrance) != 2:
        print("invalid")
    else:
        if BFS(entrance[0], entrance[1]):
            print("valid")
        else:
            print("invalid")