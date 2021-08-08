import heapq
N = int(input())
a = list(map(int, input().split()))

heap = []
for x in a:
    heapq.heappush(heap, -x)
    if len(heap) < 3:
        print(-1)
    else:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        third = -heapq.heappop(heap)
        print(first * second * third)
        heapq.heappush(heap, -first)
        heapq.heappush(heap, -second)
        heapq.heappush(heap, -third)