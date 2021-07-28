n, x = map(int, input().split())
c = list(map(int, input().split()))

res = 0
c.sort()

for i in range(n):
    res += c[i] * x
    if x > 1:
        x -= 1

print(res)