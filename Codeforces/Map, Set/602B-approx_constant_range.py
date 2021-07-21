n = int(input())
a = list(map(int, input().split()))

left = res = 0
right = -1
map = {}

while (right < n-1):
    right += 1
    if a[right] in map:
        map[a[right]] += 1
    else:
        map[a[right]] = 1

    while (len(map) > 2):
        map[a[left]] -= 1
        if map[a[left]] == 0:
            map.pop(a[left])
        left += 1

    res = max(res, right-left+1)

print(res)