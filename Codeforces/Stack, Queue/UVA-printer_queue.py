from queue import Queue

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    max_nums = []
    queue = Queue()
    freq = [0] * 10
    for i in range(n):
        if a[i] not in max_nums:
            max_nums.append(a[i])
        queue.put((i, a[i]))
        freq[a[i]] += 1

    max_nums.sort(key=lambda x:-x)
    res = 0
    while True:
        while max_nums[0] > queue.queue[0][1]:
            queue.put(queue.get())
        if queue.queue[0][0] == m:
            break
        res += 1
        queue.get()
        freq[max_nums[0]] -= 1
        if freq[max_nums[0]] == 0:
            max_nums.pop(0)
    print(res+1)