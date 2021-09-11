def FloydWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])

tc = 0
while True:
    tc += 1
    n = int(input())
    if n == 0: break

    currencies = []
    dist = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for _ in range(n):
        currencies.append(input())

    m = int(input())
    for _ in range(m):
        source, rate, target = input().split()
        u, v = currencies.index(source), currencies.index(target)
        dist[u][v] = float(rate)
    input()

    FloydWarshall()

    isArbitrage = False
    for i in range(n):
        if dist[i][i] > 1:
            isArbitrage = True
            break

    print("Case {}: {}".format(tc, "Yes" if isArbitrage else "No"))