# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10

N = int(input())
cards = list(map(int, input().split()))

# cards 정렬
cards.sort()
# -10, 2, 3, 6, 10


M = int(input())
query = list(map(int, input().split()))

def is_in_card(target):
    st = 0
    en = N-1

    while st < en:
        mid = (st+en) // 2
        if cards[mid] == target:
            return 1
        elif cards[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    if cards[st] == target:
        return 1
    else:
        return 0

for q in query:
    print(is_in_card(q), end = " ")

