# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

adj = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

st, en = map(int, input().split())

heap = []
D = [float("inf") for _ in range(N+1)]

D[st] = 0
heapq.heappush(heap, (0, st))

while heap:
    cur_w, cur_v = heapq.heappop(heap)

    # 만약 cur값이 D와 따로 놀고 있다면 버린다
    if D[cur_v] != cur_w:
        continue

    for nxt in adj[cur_v]:
        nxt_w, nxt_v = nxt[0], nxt[1]
        if D[nxt_v] <= D[cur_v] + nxt_w:
            continue
        
        D[nxt_v] = D[cur_v] + nxt_w
        heapq.heappush(heap, (D[nxt_v], nxt_v))

print(D[en])