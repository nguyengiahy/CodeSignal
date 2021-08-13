from queue import Queue
import heapq

while True:
    stack = []
    queue = Queue()
    pq = []
    isStack = isQueue = isPQ = 1
    try:
        n = int(input())
    except EOFError:
        break

    for i in range(n):
        cmd, val = map(int, input().split())
        if cmd == 1:
            stack.append(val)
            queue.put(val)
            heapq.heappush(pq, -val)
        else:
            if len(stack) > 0:
                if val != stack.pop():
                    isStack = 0
                if val != queue.get():
                    isQueue = 0
                if val != -heapq.heappop(pq):
                    isPQ = 0
            else:
                isStack = isQueue = isPQ = 0

    if isStack + isQueue + isPQ == 0:
        print("impossible")
    elif isStack + isQueue + isPQ > 1:
        print("not sure")
    else:
        if isStack:
            print("stack")
        elif isQueue:
            print("queue")
        else:
            print("priority queue")