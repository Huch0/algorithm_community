class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()

        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1]: #중복되는 숫자 처리
                continue 

            left, right = i+1, len(nums)-1 #two-pointer
            sum = 0
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else : #sum = 0
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return result