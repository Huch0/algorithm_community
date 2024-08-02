# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

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
    print(find_in_numbers(q))