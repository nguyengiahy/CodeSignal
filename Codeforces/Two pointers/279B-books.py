n, t = map(int, input().split())
arr = list(map(int, input().split()))

l = r = res = sum = 0

while r < n:
    sum += arr[r]

    while sum > t:
        sum -= arr[l]
        l += 1

    res = max(res, r-l+1)
    r += 1

print(res)