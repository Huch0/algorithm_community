def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    X = list(map(int, input().strip().split()))
    print(max_subarray_sum(X))


    """
    1806번 문제와 달리 부분합이 최대인 부분배열을 구해야 함
    이 문제의 경우 음수가 나올 때 문제가 발생하므로 '현재까지의 부분합 + 현재 원소' vs '현재 원소' 의 비교를 반복하며
    부분배열을 새로 시작할 지, 아니면 부분배열을 연장할 지 결정해야 함
    """