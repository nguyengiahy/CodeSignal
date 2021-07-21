# watch again:
# - how to check 2 strings have all same characters quickly
# - how to check if st2 can be constructed by deleting some chars from st1
# - how to check if st2 can be constructed by both deleting and swapping chars in st1

def isArray(st1, st2):
    s1 = sorted(st1)
    s2 = sorted(st2)
    return s1 == s2

def isAutomaton(st1, st2):
    j = 0
    for i in st1:
        if j == len(st2):
            break
        if i == st2[j]:
            j += 1

    return j == len(st2)

def isBoth(st1, st2):
    for i in st2:
        t = st1.find(i)
        if t == -1:
            return False
        st1 = st1[:t] + '0' + st1[t+1:]
    return True

st1 = input()
st2 = input()
if isArray(st1, st2):
    print("array")
elif isAutomaton(st1, st2):
    print("automaton")
elif isBoth(st1, st2):
    print("both")
else:
    print("need tree")