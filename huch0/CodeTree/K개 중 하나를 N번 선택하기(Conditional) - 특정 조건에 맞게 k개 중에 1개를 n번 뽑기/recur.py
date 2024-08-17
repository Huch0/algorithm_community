K, N = map(int, input().split())

answers = []


def recur(series):
    if len(series) == N:
        answers.append(series)
        return

    for i in range(1, K + 1):
        if len(series) >= 2 and i == series[-1] == series[-2]:
            continue
        recur(series + [i])


recur([])

for series in answers:
    print(' '.join(map(str, series)))
