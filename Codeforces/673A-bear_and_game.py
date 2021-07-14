n = int(input)
a = list(map(int, input().split()))

t = 0
for i in range(n):
	if t + 15 < a[i]:
		print(t+15)
		exit()
	else:
		t = a[i]

print(min(t+15, 90))