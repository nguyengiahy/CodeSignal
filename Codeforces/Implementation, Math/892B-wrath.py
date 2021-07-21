n = int(input())
a = list(map(int, input().split()))

kill = 0
res = 0

for i in range(len(a)-1,-1,-1):
    if kill == 0:
        res += 1
    kill -= 1
    kill = max(kill, a[i])

print(res)