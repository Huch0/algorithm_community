# 10 15
# 5 1 3 5 10 7 4 9 2 8

N, S = map(int, input().split())
nums = list(map(int, input().split()))

st = 0
en = 0

answer = 100000
sum = 0
while st < N and en <= N:
    if sum >= S:
        # print(st, en, sum)
        answer = min(answer, en-st)
        sum -= nums[st]
        st += 1
    else:
        if en < N:
            sum += nums[en]
        en += 1

print(answer if answer != 100000 else 0)