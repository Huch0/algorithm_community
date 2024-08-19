# 2 3
# 1 3 2
# 12 50 31
# -> 1

# 2 3
# 1 3 2 
# 12 50 10
# -> 0

# 5 3
# 20 10 30
# 10 20 60
# 80 25 79
# 30 50 80
# 80 25 81
# -> 2

from collections import defaultdict
import math

# 좌표 압축 코드
def compress_planet(planet):
    sorted_planet = list(set(planet))
    sorted_planet = sorted(sorted_planet)
    # print()
    # print(sorted_planet)
    compress = []

    for p in planet:
        st = 0
        en = len(sorted_planet)-1
        while st < en:
            mid = (st + en) // 2
            if sorted_planet[mid] > p:
                en = mid - 1
            elif sorted_planet[mid] == p:
                compress.append(mid)
                break
            elif sorted_planet[mid] < p:
                st = mid + 1
        if st == en:
            compress.append(st)
    return compress

compresses = defaultdict(list)

M, N = map(int, input().split())

for _ in range(M):
    planet = list(map(int, input().split()))
    compress = compress_planet(planet)

    # print(compress)
    compress = str(compress)
    if compresses[compress]:
        compresses[compress] += 1
    else:
        compresses[compress] = 1

# print(compresses)
sum_of_uni = 0
for value in compresses.values():
    if value == 1:
        continue
    else:
        sum_of_uni += math.comb(value, 2)

print(sum_of_uni)