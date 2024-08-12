# 4 3
# 2 5 11 7
# 9 7 4

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#B는 이분탐색을 할 것이므로 정렬
B.sort()

def is_in_B(target):
    st = 0
    en = M-1

    while st < en:
        mid = (st+en) // 2
        if B[mid] == target:
            return 1
        elif B[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    if B[st] == target:
        return 1
    else:
        return 0

# A에는 있는데 B에는 없는 원소들의 집합
A_minus_B = []

for a in A:
    if not is_in_B(a):
        A_minus_B.append(a)

if A_minus_B:
    A_minus_B.sort()
    print(len(A_minus_B))
    for e in A_minus_B:
        print(e, end = " ")

else:
    print(0)