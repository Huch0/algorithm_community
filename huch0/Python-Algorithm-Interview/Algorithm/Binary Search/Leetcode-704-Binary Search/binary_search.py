class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            # mid = (low + high) // 2
            # In languages with strict types,
            # (low + high) can cause overflow if the value exceeds the range of type.
            mid = low + (high - low) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return -1
