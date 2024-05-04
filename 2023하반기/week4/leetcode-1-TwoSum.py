class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = {}
        for i, n in enumerate(nums):
            if target - n in mydic:
                return [i, mydic[target-n]]
            mydic[n] = i

# list에 저장된 값을 찾기 위해 for문을 도는 것과 in을 쓰는 것의 시간 복잡도는 같지만 in을 쓰는쪽이 더 빠르다고 한다
# 딕셔너리에 저장된 값을 in으로 찾는것은 평균적으로 O(1)의 시간이 걸린다