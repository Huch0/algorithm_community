# 10
# 2 -5 2 3 -4 7 -4 0 1 -6
# [-6, -5, -4, -4, 0, 1, 2, 2, 3, 7]
# [-11, -10, -10, -6, -5, -4, -4, -3, 1, -9, -9, -5, -4, -3, -3, -2, 2, -8, -4, -3, -2, -2, -1, 3, -4, -3, -2, -2, -1, 3, 1, 2, 2, 3, 7, 3, 3, 4, 8, 4, 5, 9, 5, 9, 10]

import bisect

N = int(input())
A = list(map(int, input().split()))

A.sort()

result = 0

for i in range(N):
    for j in range(i+1, N):
        e = A[i] + A[j]
        left = bisect.bisect_left(A, -e, lo=j+1, hi=N)
        right = bisect.bisect_right(A, -e, lo=j+1, hi=N)
        result += right - left

print(result)