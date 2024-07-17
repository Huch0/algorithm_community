# 이친수는 0으로 시작하지 않는다.
# 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.

# 3 -> 2

N = int(input())
D = [1 for _ in range(N+1)]

if N > 2:
    for i in range(3, N+1):
        D[i] = D[i-1] + D[i-2]

print(D[N])