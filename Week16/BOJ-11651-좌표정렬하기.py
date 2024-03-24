import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n) :
    x, y = tuple(map(int,sys.stdin.readline().split()))
    heapq.heappush(heap,(y,x))

while heap :
    y,x = heapq.heappop(heap)
    print(x,y)
    

