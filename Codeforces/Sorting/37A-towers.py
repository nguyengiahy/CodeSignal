n = int(input())
a = list(map(int, input().split()))
a.sort()

num_towers = height = 1
max_height = 1
for i in range(1, n):
    if a[i] != a[i-1]:
        num_towers += 1
        height = 1
    else:
        height += 1
        max_height = max(max_height, height)

print(max_height, num_towers)