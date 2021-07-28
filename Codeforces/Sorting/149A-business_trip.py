k = int(input())
a = list(map(int, input().split()))

if k == 0:
    print(0)
    exit()

a.sort()
res = 0

for i in range(11,-1,-1):
    res += a[i]
    if res >= k:
        print(12-i)
        exit()

print(-1)