# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10

from collections import Counter

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

counter = Counter(numbers)

M = int(input())
query = list(map(int, input().split()))

def find_in_numbers(n):
    st = 0
    en = N - 1

    
    while st <= en:
        md = (en + st) // 2
        if numbers[md] == n:
            return 1
        elif numbers[md] < n:
            st = md + 1
        elif numbers[md] > n:
            en = md - 1
    
    return 0

for q in query:
    print(counter[q], end = " ")