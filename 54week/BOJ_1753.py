# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

from collections import defaultdict
import heapq
import sys

V, E = map(int, input().split())
st = int(input())
adj = defaultdict(list)

D = [float("inf") for _ in range(V+1)]

input = sys.stdin.readline

heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

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
    
for dst in D[1:]:
    if dst == float("inf"):
        print("INF")
    else:
        print(dst)
