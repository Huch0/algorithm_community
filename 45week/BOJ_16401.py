# 3 10
# 1 2 3 4 5 6 7 8 9 10
# -> 8

# 4 3
# 10 10 15
# -> 7

# M은 사람 수, N은 과자 수
M, N = map(int, input().split())

snacks = list(map(int, input().split()))
snacks.sort()

# 랜선 자르기랑 비슷한 문제
# using Parametric Search

# 내가 과자의 길이를 15로 했으면 사람이 1명만 먹을 수 있는거고
# 과자의 길이를 1로 했으면 35명이 과자를 먹는거다
# 설정하는 과자의 길이에 따라 먹을 수 있는 사람 수를 Return 하는 함수를 만들어보자

def cal_num_of_eatable_ppl(length):
    return sum([snack // length for snack in snacks])

# 과자 길이의 최솟값
st = 0

# 과자 길이의 최댓값 + 1
# +1을 하는 이유는 mid를 계산할 때 st+en을 하고 2로 나눈 몫을 반환하기 떄문
en = max(snacks) + 1
while st < en:
    mid = (st + en + 1) // 2

    if cal_num_of_eatable_ppl(mid) < M:
        en = mid - 1
    else:
        st = mid

print(st)

# 단, 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없다면, 0을 출력한다.

