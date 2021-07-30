from queue import Queue
MAX = 502
ice_map = [None] * MAX
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def isValid(x, y):
    return x in range(n) and y in range(m)

def BFS(sr, sc, fr, fc):
    q = Queue()
    q.put((sr,sc))

    while not q.empty():
        u = q.get()
        for i in range(4):
            r = u[0] + dr[i]
            c = u[1] + dc[i]

            if r == fr and c == fc  and ice_map[r][c] == 'X':
                return True

            if isValid(r,c) and ice_map[r][c] == '.':
                ice_map[r][c] = 'X'
                q.put((r,c))

    return False

n, m = map(int, input().split())
for i in range(n):
    ice_map[i] = list(input())

sr, sc = map(int, input().split())
fr, fc = map(int, input().split())

print("YES" if BFS(sr-1, sc-1, fr-1, fc-1) else "NO")