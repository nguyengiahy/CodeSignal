n = int(input())
a = list(map(int, input().split()))

c1 = c2 = 0
turn = 0

while len(a) > 0:
    n = len(a) - 1
    turn += 1
    if a[0] >= a[n]:
        if turn % 2 == 0:
            c2 += a[0]
        else:
            c1 += a[0]
        a.pop(0)
    elif a[n] > a[0]:
        if turn % 2 == 0:
            c2 += a[n]
        else:
            c1 += a[n]
        a.pop(n)

print(c1, c2)