import heapq
max_heap = []
min_heap = []
taken = [False] * 1000005
n = int(input())
idx = res = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    for x in arr[1:]:
        idx += 1
        heapq.heappush(max_heap, (-x, idx))
        heapq.heappush(min_heap, (x, idx))

    while taken[max_heap[0][1]]:    # if this receipt is already taken out before
        heapq.heappop(max_heap)
    while taken[min_heap[0][1]]:    # if this receipt is already taken out before
        heapq.heappop(min_heap)

    res += -max_heap[0][0] - min_heap[0][0]
    taken[max_heap[0][1]] = True
    taken[min_heap[0][1]] = True

print(res)