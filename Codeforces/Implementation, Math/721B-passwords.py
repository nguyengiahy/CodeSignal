n, k = map(int, input().split())
lengths = []
for _ in range(n):
    s = input()
    lengths.append(len(s))

lengths.sort()
s = input()
m = len(s)

best = 200
worst = -1
for i in range(n):
    if lengths[i] == m:
        best = min(best, i)
        worst = max(worst, i)

print(best//k * 5 + best + 1, worst//k * 5 + worst + 1)