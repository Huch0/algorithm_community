def read_int_list():
    return list(map(int, input().split())) # 자주 쓰는 구문. 익혀두기

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 # 중앙값 설정
        if array[mid] == target: # 타겟을 찾으면? 중앙값 반환
            return mid
        elif array[mid] > target: # 중앙값이 타겟보다 크다면? 왼쪽 부분 탐색
            end = mid - 1
        else: # 중앙값이 타겟보다 작다면? 오른쪽 부분 탐색
            start = mid + 1
    return None

n, target = read_int_list()
array = read_int_list()

result = binary_search(array, target, 0, n-1)
if result is None: # 결과가 리스트에 없음
    print("원소가 존재하지 않음")
else: # 결과가 있다면 결과 출력 (index는 1부터 시작하기 때문에 +1)
    print(result + 1)
