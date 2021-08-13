import heapq
while True:
    n = int(input())
    if n == 0: break
    a = list(map(int, input().split()))

    pq = []
    for x in a:
        heapq.heappush(pq, x)

    res = 0
    while len(pq) > 1:
        x1 = heapq.heappop(pq)
        x2 = heapq.heappop(pq)
        res += x1 + x2
        heapq.heappush(pq, x1 + x2)
    print(res)