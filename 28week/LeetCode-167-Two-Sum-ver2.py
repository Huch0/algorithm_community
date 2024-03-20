class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # TLE (Time Limit Exceeded)

        # left, right = 0, 1
        # while left < len(numbers) - 1:
        #     if numbers[left] + numbers[right] == target:
        #         return [left + 1, right + 1]
        #     elif numbers[left] + numbers[right] < target:
        #         right += 1
        #     else:
        #         left += 1
        #         right = left + 1

        #     if right == len(numbers):
        #         left += 1
        #         right = left + 1

        def binary_search(left, target):
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == target:
                    return mid
                elif numbers[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
    
        for i in range(len(numbers) - 1):
            j = binary_search(i+1, target - numbers[i])
            if j != -1:
                return [i + 1, j + 1]