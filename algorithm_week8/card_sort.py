import heapq

num_bundle = int(input())
cards = []
for i in range(num_bundle):
    num_cards = int(input())
    cards.append(num_cards)

# Python의 heapq는 최소 힙. 바로 사용
heapq.heapify(cards)
# card의 수들이 담긴 리스트로 최소 힙을 바로 구성

result = 0

while len(cards) > 1:
    # 제일 적은 수의 카드묶음 두 개를 선택(cards에서 pop하는 방식)
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    # 카드묶음 두개 합친 수를 sum_card에 저장.
    sum_card = card1 + card2
    result += sum_card

    # sum_card를 다시 힙에 삽입.
    heapq.heappush(cards, sum_card)

print(result)
