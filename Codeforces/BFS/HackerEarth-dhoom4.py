from queue import Queue
MAX = 100000 + 5
MOD = 100000

def BFS(s, f):
    q = Queue()
    q.put(s)
    distance = [0] * MAX

    while not q.empty():
        u = q.get()

        for key in keys:
            v = (u * key) % MOD
            if not distance[v]:
                q.put(v)
                distance[v] = distance[u] + 1
                if v == f:
                    return distance[v]

    return -1

s, f = map(int, input().split())
n = int(input())
keys = list(map(int, input().split()))
print(BFS(s,f))