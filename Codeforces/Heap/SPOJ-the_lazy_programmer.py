import heapq

t = int(input())
for _ in range(t):
    n = int(input())

    tasks = []
    for _ in range(n):
        a, b, d = map(int, input().split())
        tasks.append((d, a, b))

    tasks.sort()

    pq = []
    time = money = 0
    for i in range(n):
        d, a, b = tasks[i]
        time += b
        heapq.heappush(pq, (-a, b, d))
        while time > d:
            top_a, top_b, top_d = heapq.heappop(pq)
            if top_b > time - d:
                money += (time - d) / -top_a
                top_b -= time - d
                time = d
                heapq.heappush(pq, (top_a, top_b, top_d))
            else:
                money += top_b / -top_a
                time -= top_b

    print("%.2f" %money)