n = int(input())
a = list(map(int, input().split()))

clone = sorted(a)

for i in range(n):
    for j in range(n):
        if clone[j] > a[i]:
            break
    if clone[j] == a[i]:
        j = n
    print(n - j + 1, end=" ")