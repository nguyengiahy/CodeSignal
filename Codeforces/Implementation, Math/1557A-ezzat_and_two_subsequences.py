t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    avg_left = sum(arr[0:n-1]) / (n-1)
    res = avg_left + arr[n-1]

    print(res)