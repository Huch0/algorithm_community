N, K = map(int, input().split())
A = list(map(int, input().split()))

num_cnt = [0] * 100001

s, e = 0, 0
ans = 0

while e < N:
    num_cnt[A[e]] += 1
    while num_cnt[A[e]] > K:
        num_cnt[A[s]] -= 1
        s += 1

    ans = max(ans, e-s+1)
    e += 1

print(ans)
