l = int(input())
st = list(input())
for i in range(l):
    st[i] = st[i].lower()
st.sort()
res = 1
for i in range(1, l):
    if st[i] != st[i-1]:
        res += 1

print("YES" if res == 26 else "NO")