t = int(input())

for i in range(t):
    st = input()
    count = res = 0
    for j in range(len(st)):
        if st[j] == "<":
            count += 1
        else:
            count -= 1
        if count == 0:
            res = j+1
        if count < 0:
            break
    print(res)