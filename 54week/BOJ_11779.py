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

V = int(input())
E = int(input())

input = sys.stdin.readline
adj = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

st, en = map(int, input().split())
D = [float("inf") for _ in range(V+1)]
pre = [0 for _ in range(V+1)]

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
        pre[nv] = cur_v
        heapq.heappush(heap, (D[nv], nv))


print(D[en])

path = []
i = en
while pre[i] != 0:
    path.append(i)
    i = pre[i]

path.append(st)
print(len(path))
path.reverse()
for p in path:
    print(p, end = " ")
print()