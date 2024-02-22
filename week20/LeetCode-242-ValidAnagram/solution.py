class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_0 = 0
        cnt_2 = len(nums) - 1 
        cnt_1 = cnt_0
        for i in range(len(nums)):
            while i <= cnt_2 and nums[i] == 2:
                nums[i], nums[cnt_2] = nums[cnt_2], nums[i]
                cnt_2 -= 1

            while cnt_0 <= i and nums[i] == 0:
                nums[i], nums[cnt_0] = nums[cnt_0], nums[i]
                cnt_0 += 1

            if cnt_0 <= i <= cnt_2 and nums[i] == 1:
                cnt_1 = i
