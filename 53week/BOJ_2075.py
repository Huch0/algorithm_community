# 5
# 12 7 9 15 5
# 13 8 11 19 6
# 21 10 26 31 16
# 48 14 28 35 25
# 52 20 32 41 49

# 35

import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])
    
# for i in range(N):
#     heap.append((-matrix[-1][i], N-1, i))

# result = 0
# for i in range(N):
#     result, x, y = heapq.heappop(heap)
#     heapq.heappush(heap, (-matrix[x-1][y], x-1, y))

# print(-result)