import heapq
import sys
minheap = []

N=int(sys.stdin.readline())

for _ in range(N):
    n=int(sys.stdin.readline())
    if n==0:
        if not minheap:
            print(0)
        else:
            print(heapq.heappop(minheap))
    else:
        heapq.heappush(minheap, n)