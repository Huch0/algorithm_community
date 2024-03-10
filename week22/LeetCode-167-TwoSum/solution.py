class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not (left == right):
            tmp = numbers[left] + numbers[right]
            if tmp > target:
                right -= 1
            elif tmp < target:
                left += 1
            else:
                return [left + 1, right + 1]
