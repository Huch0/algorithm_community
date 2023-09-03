class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        result = []
        for i, num in enumerate(nums):
            rest_permutes = self.permute(nums[:i] + nums[i+1:])
            for perm in rest_permutes:
                result.append([num] + perm)
                
        return result

