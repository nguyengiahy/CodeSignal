def minHeapify(i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(heap) and heap[left] < heap[smallest]:
        smallest = left
    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        minHeapify(smallest)

def buildHeap(n):
    for i in range(n//2 - 1, -1, -1):
        minHeapify(i)

def top():
    return heap[0]

def push(val):
    heap.append(val)
    i = len(heap) - 1
    while i > 0:
        parent = (i-1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

def pop():
    n = len(heap)
    if n == 0:
        return
    heap[0] = heap[n-1]
    heap.pop()
    minHeapify(0)

if __name__ == "__main__":
    heap = [7, 12, 6, 10, 17, 15, 2, 4]
    buildHeap(len(heap))
    print(heap)
    push(3)
    print(heap)
    pop()
    print(heap)