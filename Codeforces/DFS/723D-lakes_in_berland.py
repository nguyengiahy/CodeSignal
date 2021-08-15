MAX = 50 + 5
visited = [[False] * MAX for _ in range(MAX)]
grid = [[] for _ in range(MAX)]
lakes = []
dr = [0, 0, 1, -1]
dc = [1, -1, 0 ,0]

def isValid(r, c):
    return r in range(n) and c in range(m)

def onBorder(r, c):
    return r == 0 or c == 0 or r == n-1 or c == m-1

def DFS(s):
    global lakes
    stack = []
    stack.append(s)
    visited[s[0]][s[1]] = True

    isOcean = False
    temp = []

    while len(stack) > 0:
        u = stack.pop()
        temp.append((u[0], u[1]))

        if onBorder(u[0], u[1]):
            isOcean = True

        for i in range(4):
            r = u[0] + dr[i]
            c = u[1] + dc[i]
            if isValid(r, c) and grid[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                stack.append((r, c))

    if not isOcean:
        lakes.append(temp)

n, m, k = map(int, input().split())

# Read input
for i in range(n):
    grid[i] = list(input())

# Find lakes
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' and not visited[i][j]:
            DFS((i, j))

# Fill lakes to have exactly k lakes left (minimum number of cells filled)
lakes.sort(key=lambda lake: len(lake))  # Sort to have minimum number of cells filled
res = 0
for i in range(len(lakes) - k):
    res += len(lakes[i])
    for r, c in lakes[i]:
        grid[r][c] = '*'

# Print result
print(res)
for i in range(n):
    print(''.join(grid[i]))