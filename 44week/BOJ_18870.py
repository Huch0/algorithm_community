# 5
# 2 4 -10 4 -9

from collections import Counter

N = int(input())
numbers = list(map(int, input().split()))

counter = Counter(numbers)
numbers_u = [n for n in counter.keys()]
numbers_u.sort()

# print(numbers_u)

def lower_bound(x):
    st = 0
    en = len(numbers_u)
    while st < en:
        mid = (st + en) // 2
        if numbers_u[mid] == x:
            return mid
        elif numbers_u[mid] < x:
            st = mid + 1
        else:
            en = mid
    return st

for n in numbers:
    print(lower_bound(n), end = " ")