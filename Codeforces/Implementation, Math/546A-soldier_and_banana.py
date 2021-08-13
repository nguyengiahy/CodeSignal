k, n, w = map(int, input().split())

res = 0
for i in range(1, w+1):
    res += k*i

print(res - n if res > n else 0)