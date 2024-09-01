# 1~400만까지 소수들 리스트 만들기

primes = [True] * 4000001
for i in range(2, 4000001):
    if primes[i]:
        for j in range(i*2, 4000001, i):
            primes[j] = False

primes = [i for i in range(2, 4000001) if primes[i]]

# print(primes)
N = int(input())

if N == 1:
    print(0)

else:
    st = 0
    en = 0
    sum = 0
    answer = 0

    while st < len(primes) and en <= len(primes):
        if sum >= N:
            if sum == N:
                answer += 1
            sum -= primes[st]
            st += 1
        else:
            if en < len(primes):
                sum += primes[en]
                en += 1
            else:
                break

    print(answer)