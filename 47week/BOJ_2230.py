# 3 3
# 1
# 5
# 3

N, M = map(int, input().split())

nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()

st = 0
en = 0

answer = 2000000000

while st < N and en < N:
    diff = nums[en] - nums[st]

    if diff >= M:
        answer = min(answer, diff)
        st += 1
    else:
        en += 1

print(answer)
# 이전 풀이
# l = 0
# r = N-1

# while nums[r]-nums[l] >= M:
#     l += 1
#     r -= 1

# case1 = nums[r+1] - nums[l]
# case2 = nums[r] - nums[l-1]
# case3 = nums[r+1] - nums[l-1]

# if case1 < M and case2 < M:
#     print(case3)
# elif M <= case1 <= case2 or case2 < M :
#     print(case1)
# elif M <= case2 < case1 or case1 < M:
#     print(case2)
