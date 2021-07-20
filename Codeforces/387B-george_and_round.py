n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=False)
b.sort(reverse=False)
res = 0

j = 0
for i in range(len(a)):
	if b[j] < a[i]:
		res += 1
	else:
		j += 1

print(res)