class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = len(nums)

        while white < blue :
            if nums[white] < 1 :
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] > 1 :
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]
            else :
                white += 1
            print(nums)