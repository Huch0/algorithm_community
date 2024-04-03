class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sums = [0]

        for i in range(0, len(nums)):
            sums.append(nums[i] + sums[i])
        
        stack = [0]
        results = []
        
        for i in range(len(sums)):
            if sums[i] < stack[0]:
                results.append(stack[-1] - stack[0])
                stack = [sums[i]]
            elif sums[i] > stack[-1]:
                stack.append(sums[i])
                #print(stack)

        results.append(stack[-1] - stack[0])
        
        if any([result > 0 for result in results]):
            return max(results)
        else:
            return max(nums)