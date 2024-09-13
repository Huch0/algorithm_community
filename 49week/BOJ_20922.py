# 9 2
# 3 2 5 5 6 4 4 5 7
# -> 7

N, K = map(int, input().split())
nums = list(map(int, input().split()))

t = [0 for _ in range(100001)]

answer = 0
cur_max = 0
st = 0
en = 0

while en < N:
    t[nums[en]] += 1
    cur_max = max(cur_max, t[nums[en]])

    if cur_max > K:
        answer = max(answer, en-st)

    en += 1

    while cur_max > K:
        t[nums[st]] -= 1
        if nums[st] == nums[en-1]:
            cur_max -= 1
        st += 1
    
answer = max(answer, en-st)
print(answer)