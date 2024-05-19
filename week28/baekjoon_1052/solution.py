N ,K = map(int, input().split())
buy_bottle = list()
i = 0

while N != 1:
    i = i + 1
    if N % 2 == 1:
        buy_bottle.append(2 ** (i -1))
    N = N // 2

max_bottle = 2 ** i

if buy_bottle and len(buy_bottle) + 1 > K:
    reduce = (len(buy_bottle) + 1) - K
    if reduce == len(buy_bottle):
        print(max_bottle - sum(buy_bottle))
    else:
        print(buy_bottle[reduce] - sum(buy_bottle[:reduce]))
else:
    print(0)