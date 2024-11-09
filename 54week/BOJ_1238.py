# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3

import heapq
import sys
from collections import defaultdict

N, M, X = map(int, input().split())

adj = defaultdict(list)
input = sys.stdin.readline
results = [0 for _ in range(N+1)]
heap = []

for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

for st in range(N+1):
    if st == 0:
        continue

    D = [float("inf") for _ in range(N+1)]
    D[st] = 0
    
    heapq.heappush(heap, (0, st))

    while heap:
        cur_w, cur_v = heapq.heappop(heap)
        
        # 만약 cur값이 D와 따로 놀고 있다면 버린다
        if D[cur_v] != cur_w:
            continue

        for nxt in adj[cur_v]:
            nw, nv = nxt[0], nxt[1]
            if D[nv] <= D[cur_v] + nw:
                continue
            D[nv] = D[cur_v] + nw
            heapq.heappush(heap, (D[nv], nv))

    if st == X:
        for en in range(1, N+1):
            if en == X:
                continue
            results[en] += D[en]
    else:
        results[st] += D[X]

print(max(results))

