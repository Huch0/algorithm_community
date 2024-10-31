# 4 2
# 9 7 9 1

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()


result = [0 for _ in range(M)]
is_used = [False for _ in range(N)]

def nm_9(d):
    if d == M:
        for r in result:
            print(r, end = " ")
        print()
    else:
        is_duplicated = []
        for i in range(N):
            # d를 결정 짓는 것은 numbers에서 이미 사용한 것을 제외하고 중복을 허용하면 안된다.
            if is_used[i]:
                continue
            if not is_duplicated or numbers[i] != is_duplicated[-1]:
                is_duplicated.append(numbers[i])
                result[d] = numbers[i]
                is_used[i] = True
                nm_9(d+1)
                is_used[i] = False
            else:
                continue

nm_9(0)