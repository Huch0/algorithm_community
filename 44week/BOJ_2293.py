# 5
# 2
# 3
# 5
# 10
# 18

N = int(input())

U = []
for _ in range(N):
    U.append(int(input()))

U.sort()

U_two = []
for i in range(N):
    for j in range(N):
        U_two.append(U[i]+U[j])
U_two.sort()

def fine_U_two(num):
    st = 0
    en = len(U_two) - 1
    while st < en:
        mid = (st+en)//2
        if U_two[mid] == num:
            return mid
        elif U_two[mid] < num:
            st = mid+1
        else:
            en = mid-1
    return -1

find_flag = False
for i in range(N-1, -1, -1):
    target = U[i]
    # print()
    # print(target)
    for j in range(i-1, -1, -1):
        if fine_U_two(target - U[j]) >= 0:
            find_flag = True
            break

    if find_flag:
        print(target)
        break