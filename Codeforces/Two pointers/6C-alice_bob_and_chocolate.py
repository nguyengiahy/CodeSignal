n = int(input())
a = list(map(int, input().split()))

i = 0
j = n-1
t1 = a[i]
t2 = a[j]

while i<j-1:
    if t1 <= t2:
        i += 1
        t1 += a[i]
    elif t1 > t2:
        j -= 1
        t2 += a[j]

print(i+1, n-j)