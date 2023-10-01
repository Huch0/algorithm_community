def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0
#클래식한 이진탐색 함수

n = int(input())
array = list(map(int, input().split()))
array.sort()  # 정렬이 돼 있는 리스트에서 이진 탐색을 할 수 있다!!
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(binary_search(array, target, 0, n-1))


A = set(map(int, input().split()))  # 리스트가 아닌 set으로 입력받기.
# 파이썬 에서 set 메소드는 기본적으로 해시테이블을 구성한다. 해시테이블은 탐색이 굉장히 빠르므로 이진탐색보다 간단하고 빠르게 탐색 가능.
numbers = list(map(int, input().split()))

def using_set_method():
    for num in numbers:
        if num in A:
            print(1)
        else:
            print(0)
