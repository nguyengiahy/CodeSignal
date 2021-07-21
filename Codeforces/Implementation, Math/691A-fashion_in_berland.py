n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in arr:
    if i:
        count += 1

if (n==1 and count==1) or (n>1 and count==n-1):
    print("YES")
else:
    print("NO")