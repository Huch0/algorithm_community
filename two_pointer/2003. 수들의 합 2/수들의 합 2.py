N, M = map(int, input().split())
A = list(map(int, input().split()))

s, e = 0, 0
cnt = 0
cur = 0

while(e < N):
    cur = sum(A[s:(e+1)])
    if cur == M:
        cnt += 1
        s += 1
        e += 1
    elif cur < M:
        e += 1
    else:
        s += 1

print(cnt)