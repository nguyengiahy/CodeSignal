n, k = map(int, input().split())
a = list(map(int, input().split()))

s = set()
t = set()
l = r = -1
found_r = found_l = False

for i in range(n):
    s.add(a[i])
    if len(s) == k:
        found_r = True
        r = i
        break

s.clear()
for i in range(r,-1,-1):
    s.add(a[i])
    if len(s) == k:
        found_l = True
        l = i
        break

if found_l and found_r:
    print(l+1, r+1)
else:
    print(-1, -1)