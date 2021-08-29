INF = (1 << 30) * 100 + 7
tc = 0

def BellmanFord(s):
    dist[s][s] = 0
    for i in range(n-1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
                dist[s][v] = dist[s][u] + w

    for i in range(n - 1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
                dist[s][v] = -INF

while True:
    tc += 1
    n = int(input())
    if n == 0: break

    cities = []
    graph = []
    for i in range(n):
        line = input().split()
        cities.append(line[0])
        for j in range(1, n+1):
            u = i
            v = j-1
            weight = int(line[j])
            if u != v and weight == 0: continue
            if u == v and weight >= 0: weight = 0
            graph.append((u, v, weight))
    m = len(graph)

    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        BellmanFord(i)

    print("Case #" + str(tc) + ":")
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        if dist[s][t] == INF:
            print(cities[s] + "-" + cities[t] + " NOT REACHABLE")
        elif dist[s][t] == -INF:
            print("NEGATIVE CYCLE")
        else:
            print(cities[s] + "-" + cities[t] + " " + str(dist[s][t]))