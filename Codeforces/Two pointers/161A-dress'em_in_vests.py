n,m,x,y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0
count = 0
vest = []

while i < n and j < m:
    if a[i] + y < b[j]:
        i += 1
    elif a[i] - x > b[j]:
        j += 1
    else:
        count += 1
        vest.append((i,j))
        i += 1
        j += 1

print(count)
for i in range(len(vest)):
    print(vest[i][0] + 1, vest[i][1] + 1)