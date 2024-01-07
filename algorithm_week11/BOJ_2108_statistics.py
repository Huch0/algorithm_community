import sys
from collections import Counter
N = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])

print(round(sum(numbers) / N))

print(numbers[N // 2])

count_list = sorted(Counter(numbers).items(), key = lambda x : (-x[1], x[0]))
if N == 1:
    print(numbers[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])

print(max(numbers) - min(numbers))