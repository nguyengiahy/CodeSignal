n = int(input())
a = list(map(int, input().split()))
left = right = 0

for i in range(n-1):
    if a[i] > a[i+1]:
        left = i
        break

right = left
while right < n-1 and a[right] > a[right+1]:
    right = right + 1

b = sorted(a)
a[left:right+1] = sorted(a[left:right+1])

if a == b:
    print("yes")
    print(left + 1, right + 1)
else:
    print("no")