def quickSort(A, low, high): 
    # 배열을 pivot을 기준으로 두 부분으로 나누고, pivot의 최종 위치를 반환
    def partition(low, high): 
        pivot = A[high]  # pivot을 배열의 마지막 요소로 선택
        left = low 
        for right in range(low, high): 
            if A[right] < pivot:  # 현재 요소가 pivot보다 작은 경우 swap
                A[left], A[right] = A[right], A[left]  
                left += 1 
        A[left], A[high] = A[high], A[left] # pivot을 최종 위치로 이동
        return left  # pivot의 index 반환
        
    if low < high:  #low가 high보다 작을 경우에만 실행
        pivotIdx = partition(low, high)  # pivot을 기준으로 배열을 두 부분으로 나눔
        quickSort(A, low, pivotIdx-1)  # pivot의 왼쪽 부분을 재귀적으로 정렬
        quickSort(A, pivotIdx+1, high)  # pivot의 오른쪽 부분을 재귀적으로 정렬
 
if __name__ == '__main__':
    n = int(input())  # 배열 크기
    A = list(map(int, input().split()))  # 배열 입력

    quickSort(A, 0, n-1)  # quicksort 진행

    for i in range(n):
        print(A[i], end=' ') # 정렬된 배열 출력