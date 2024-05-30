class Solution:
    index = 0
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        if len(nums) == 0 : return -1
        if len(nums) == 1 :
            if nums[0] == target : return self.index
            else : return -1
        
        mid = len(nums)//2
        
        if nums[mid] == target :
            return self.index + mid
        elif nums[mid] < target :
            self.index += mid
            return self.search(nums[mid:],target)
        else :
            return self.search(nums[:mid],target)