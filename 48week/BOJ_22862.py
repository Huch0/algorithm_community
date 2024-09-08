# 8 2
# 1 2 3 4 5 6 7 8
# 0 1 0 1 0 1 0 1
# -> 3

N, K = map(int, input().split())
A = list(map(int, input().split()))
# A는 짝수는 1로 / 홀수는 0으로 표현되어있음
A = [1 if i % 2 == 0 else 0 for i in A]

st = 0
en = 0
answer = 0

# 1의 개수를 최대한 늘려야한다. 그리고 1과 1사이의 0의 개수는 최대 K개까지 허용한다.
# en을 늘리면서 st와 en 사이에 0의 개수가 K개가 되면 st를 늘린다.

zero_cnt = 0
while en < N:
    if zero_cnt <= K:   
        if A[en] == 0:
            zero_cnt += 1
        en += 1
    else:
        if A[st] == 0:
            zero_cnt -= 1
        st += 1

    # debug
    # print(st, en, zero_cnt, A[st:en])
    answer = max(answer, en - st - zero_cnt)
    
print(answer)