class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #only considered ten's digit
        if not nums:
            return ""  

        ans = ""
        num_cnt = [0] * 11
        for i in range(len(nums)):
            if nums[i] < 10:
                nums[i] = nums[i] * 11
                
        sorted_nums = sorted(nums, reverse=True)
        for num in sorted_nums:
            if num % 11 == 0:
                ans += str(f"{num // 11}")
            else:
                ans += str(num)
        
        return ans