# 4 2
# 1 1 1 1
# -> 3

# 10 5
# 1 2 3 4 2 5 3 1 1 2
# -> 3

N, M = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
left = 0
right = 0

sum = 0
while left < N and right <= N:
    if sum == M:
        if right != N:
            sum += A[right]
        answer += 1
        sum -= A[left]
        left += 1
        right += 1
    elif sum < M:
        if right != N:
            sum += A[right]
        right += 1
    else:
        sum -= A[left]
        left += 1

print(answer)