import heapq
pq = []
pqremove = []
Q = int(input())
for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        heapq.heappush(pq, cmd[1])
    elif cmd[0] == 2:
        heapq.heappush(pqremove, cmd[1])
    else:
        if len(pq) > 0:
            while len(pqremove) > 0 and pqremove[0] == pq[0]:
                heapq.heappop(pq)
                heapq.heappop(pqremove)
            print(pq[0])