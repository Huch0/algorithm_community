def min_subarray_length_two_pointers(N, S, array):
    min_length = N + 1
    current_sum = 0
    start = 0

    for end in range(N):
        current_sum += array[end]
        while current_sum >= S:
            min_length = min(min_length, end - start + 1)
            current_sum -= array[start]
            start += 1

    return min_length if min_length <= N else 0

N, S = map(int, input().split())
array = list(map(int, input().split()))

print(min_subarray_length_two_pointers(N, S, array))

    """ 
    브루트 포스가 아닌 슬라이딩 윈도우 방식을 이용해서 문제 해결.
    브루트 포스는 O(n^2), 슬라이딩 윈도우는 배열을 한 번만 훑으면 되므로 O(n).
    앞으로 '최소 길이 부분합'을 구해야 하는 상황에서는 슬라이딩 윈도우를 사용.
    """