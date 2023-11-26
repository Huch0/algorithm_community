def find_closest_to_zero(N, solutions):
    solutions.sort()
    left, right = 0, N-1
    closest_sum = solutions[left] + solutions[right]
    
    while left < right:
        current_sum = solutions[left] + solutions[right]
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
        
        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            break

    return closest_sum

N = int(input().strip())
solutions = list(map(int, input().strip().split()))

print(find_closest_to_zero(N, solutions))

    """
    left와 right라는 두 개의 포인터를 사용해서, 합이 0에 가장 가까운 부분배열을 찾는다.
    용액 특성값들의 합과 0을 비교해서 포인터들을 이동시킨다.
    이러한 알고리즘을 Two Pointer Algorithm이라고 한다. 부분합 문제에서 종종 사용하자.
    """