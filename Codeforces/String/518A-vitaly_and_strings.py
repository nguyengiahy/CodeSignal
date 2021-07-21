st1 = list(input())
st2 = list(input())

n = len(st1)

for i in range(n-1,-1,-1):
    if (st1[i] == 'z'):
        st1[i] = 'a'
    else:
        st1[i] = chr(ord(st1[i]) + 1)
        break

print(''.join(st1) if st1 != st2 else "No such string")