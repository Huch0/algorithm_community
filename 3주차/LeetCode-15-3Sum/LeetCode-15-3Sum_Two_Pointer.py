class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = num + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    elem =[num, nums[left], nums[right]]
                    if elem not in result:
                        result.append(elem)
                        
                    left += 1
                    right -= 1


        return result
        
