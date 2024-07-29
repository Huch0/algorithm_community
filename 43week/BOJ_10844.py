#1 -> 9
#2 -> 17
# 0으로 시작하는 수는 계단수가 아니다.
#1,000,000,000으로 나눈 나머지 출력

N = int(input())

# N == 1일 때 9인건 당연
# N == 2일 때 17인건 9개의 경우에 대해서
# 10의 자리수가 9일 때 1의 자리수가 8만 허용된다
# N == 3이면
# 10_, 89_ 를 주의

# 10
# 89
# 


D = [1 for _ in range(10)]
step_D = [1 for _ in range(10)]
D[0] = 0

for i in range(1, N):
    step_D = D[::]
    for j in range(10):
        if 0 < j < 9:
            D[j] = (step_D[j+1] + step_D[j-1]) % 1000000000
        elif j == 0:
            D[j] = step_D[j+1] % 1000000000
        elif j == 9:
            D[j] = step_D[j-1] % 1000000000

# print(D)
print(sum(D)%1000000000)