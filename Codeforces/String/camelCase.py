st = input()
res = 1
for i in range(len(st)):
    if st[i].isupper():
        res += 1
print(res)