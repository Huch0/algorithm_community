# 18
# 1
# -1
# 0
# 0
# 0
# 1
# 1
# -1
# -1
# 2
# -2
# 0
# 0
# 0
# 0
# 0
# 0
# 0

import heapq
import sys

input = sys.stdin.readline

heap = []
N = int(input())

results = []
for _ in range(N):
    query = int(input())
    if query == 0:
        if not heap:
            results.append("0\n")
        else:
            results.append(f"{heapq.heappop(heap)[1]}\n")
    else:
        heapq.heappush(heap, (abs(query), query))

sys.stdout.write("".join(results))