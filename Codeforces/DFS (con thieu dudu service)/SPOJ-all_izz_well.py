MAX = 100 + 5
phrase = "ALLIZZWELL"
dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]

def isValid(r, c):
    return r in range(N) and c in range(M)

def DFS(r, c, idx):
    global res
    if idx == 9:
        res = "YES"
        return
    else:
        for i in range(8):
            x = r + dr[i]
            y = c + dc[i]
            if isValid(x, y) and not visited[x][y] and grid[x][y] == phrase[idx + 1]:
                visited[x][y] = True
                DFS(x, y, idx + 1)
                visited[x][y] = False
    return False


t = int(input())
for _ in range(t):
    N, M = map(int, input().split())

    start_positions = []
    grid = [[] for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    for i in range(N):
        grid[i] = list(input())
        for j in range(M):
            if grid[i][j] == 'A':
                start_positions.append((i, j))
                visited[i][j] = True

    res = "NO"
    for r, c in start_positions:
        DFS(r, c, 0)
        if res == "YES": break

    print(res)
    input()