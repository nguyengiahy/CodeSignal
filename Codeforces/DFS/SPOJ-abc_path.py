MAX = 50 + 5
grid = [[None] for _ in range(MAX)]
dist = [[1] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]
case = 0
dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]

def isValid(r, c):
    return r in range(n) and c in range(m)

def DFS(s):
    stack = []
    stack.append(s)
    visited[s[0]][s[1]] = True
    local_res = 1

    while len(stack) > 0:
        u = stack.pop()
        for i in range(8):
            r = u[0] + dr[i]
            c = u[1] + dc[i]

            if isValid(r,c) and not visited[r][c] and ord(grid[r][c]) - ord(grid[u[0]][u[1]]) == 1:
                stack.append((r, c))
                visited[r][c] = True
                dist[r][c] = dist[u[0]][u[1]] + 1
                local_res = max(local_res, dist[r][c])
    return local_res

while True:
    case += 1
    n, m = map(int, input().split())
    start_position = []
    if not n and not m: break
    for i in range(n):
        grid[i] = list(input())
        for j in range(m):
            visited[i][j] = False
            dist[i][j] = 1
            if grid[i][j] == 'A':
                start_position.append((i, j))

    res = 0
    for i in range(len(start_position)):
        res = max(res, DFS(start_position[i]))
    print("Case", str(case) + ":", res)