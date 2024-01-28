import sys
from heapq import *
input = sys.stdin.readline
pq = []
n = int(input())
for _ in range(n):
    tmp = int(input())
    heappush(pq, tmp)

ans = 0
for _ in range(n-1):
    card1 = heappop(pq)
    card2 = heappop(pq)
    card1 = card1 + card2
    ans += card1
    heappush(pq, card1)

print(ans)