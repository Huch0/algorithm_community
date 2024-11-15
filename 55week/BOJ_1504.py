# 4 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 2 3

from collections import defaultdict
import heapq
import sys

N, E = map(int, input().split())

input = sys.stdin.readline
adj = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
    adj[v].append((w, u))

v1, v2 = map(int, input().split())
D1 = [float("inf") for _ in range(N+1)]
D2 = [float("inf") for _ in range(N+1)]

def dijkstra(st, D):
    heap = []
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
    return D

D1 = dijkstra(v1, D1)
D2 = dijkstra(v2, D2)


if D1[1] == float("inf") or D1[N] == float("inf"):
    print(-1)
else:
    # 1->v1->v2->N 이 1->v2->v1->N 중 더 나은 경로를 선택한다
    print(min(D1[1] + D2[N], D1[N] + D2[1]) + D1[v2]) 
    