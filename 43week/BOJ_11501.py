# 3
# 3
# 10 7 6
# 3
# 3 5 9 
# 5
# 1 1 3 1 2

T = int(input())

results = []
for _ in range(T):
    # 입력 처리
    N = int(input())
    prices = list(map(int, input().split()))

    # 최대 이득 계산
    # 1. 주식을 사거나
    # 2. 주식을 팔거나
    # 3. 관망

    prices.reverse()

    sum = 0
    sell_point = 0
    for p in prices:
        if p > sell_point:
            sell_point = p
            continue
        sum += sell_point - p
        
    # 최대 이득 출력
    results.append(sum)

for r in results:
    print(r)