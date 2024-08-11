from collections import deque
N = int(input())

ropes = [int(input()) for _ in range(N)]

ropes.sort()
k = 0
for i in range(N):
    tmp = ropes[i] * (N-i)
    if tmp > k:
        k = tmp

print(k)
