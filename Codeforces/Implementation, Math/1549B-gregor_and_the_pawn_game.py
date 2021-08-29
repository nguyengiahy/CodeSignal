def check(i, j):
    if graph[i-1][j] == 0:
        graph[i-1][j] = 2
        return 1
    elif j-1 >= 0 and graph[i-1][j-1] == 1:
        graph[i - 1][j - 1] = 2
        return 1
    elif j+1 < n and graph[i-1][j+1] == 1:
        graph[i - 1][j + 1] = 2
        return 1
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(2)]
    graph[0] = list(map(int, input()))
    graph[1] = list(map(int, input()))
    res = 0
    for i in range(n):
        if graph[1][i] == 1:
            res += check(1, i)
    print(res)