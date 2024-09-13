# 4
# Baha enter
# Askar enter
# Baha leave
# Artem enter

# -> 
# Askar
# Artem

from collections import defaultdict
import heapq

N = int(input())

T = defaultdict(str)
heap = []

for _ in range(N):
    line = input().split()
    T[line[0]] = line[1]

for key, value in T.items():
    if value == "enter":
        heapq.heappush(heap, key)

answer = []
while heap:
    answer.append(heapq.heappop(heap))

answer.reverse()
for a in answer:
    print(a)