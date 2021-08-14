import heapq
N = int(input())
top_reviews = []    # min heap
rest_reviews = []   # max heap
count = 0
for _ in range(N):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        count += 1
        val = cmd[1]
        if len(top_reviews) > 0 and val > top_reviews[0]:
            heapq.heappush(rest_reviews, -heapq.heappop(top_reviews))
            heapq.heappush(top_reviews, val)
        else:
            heapq.heappush(rest_reviews, -val)
        if count % 3 == 0:
            heapq.heappush(top_reviews, -heapq.heappop(rest_reviews))
    else:
        if len(top_reviews) > 0:
            print(top_reviews[0])
        else:
            print("No reviews yet")