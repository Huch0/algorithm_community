# 13
# 0
# 1
# 2
# 0
# 0
# 3
# 2
# 1
# 0
# 0
# 0
# 0
# 0

import heapq
import sys

input = sys.stdin.readline
heap = []
results = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            results.append(-1*heapq.heappop(heap))
        else:
            results.append(0)
    else:
        heapq.heappush(heap, -x)

for r in results:
    print(r)