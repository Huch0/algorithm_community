# 4
# 10
# 20
# 21
# 22

# 10+20 /  / 60+40

import heapq
import sys

input = sys.stdin.readline

N = int(input())
cards = []

for _ in range(N):
    card = int(input())
    heapq.heappush(cards, card)

if N == 1:
    print(0)

else:
    # basic
    # 1. 카드에서 최솟값인 2장을 뽑아서 더한다
    # 2. 값을 다시 힙에 넣는다
    # 3. heap이 없어질 때까지 반복한다.
    result = 0
    while cards:
        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        
        result += card1+card2
        if cards:
            heapq.heappush(cards, card1+card2)
        else:
            break
    print(result)

# trick 1.
# sum_card = -1 * sum(cards)
# result = sum_card
# for i in range(len(cards)-2):
#     card = heapq.heappop(cards)
#     sum_card += card
#     result += sum_card

# print(result)
