from sys import stdin
import heapq

n = int(stdin.readline())
min_heap = []
max_heap = []
turn = 0
for _ in range(n):
    x = int(stdin.readline())
    if turn == 0:
        heapq.heappush(max_heap, (-x, x))
    else:
        heapq.heappush(min_heap, (x, x))

    if len(max_heap) and len(min_heap) and max_heap[0][1] > min_heap[0][1]:
        xa, xb = heapq.heappop(max_heap)
        na, nb = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-na, nb))
        heapq.heappush(min_heap, (-xa, xb))
    print(max_heap[0][1])
    turn = 1 - turn
    

    
