class Solution:
    def search(self, nums: List[int], target: int) -> int:
        list_size = len(nums)
        start = 0
        end = list_size - 1
        cur = (start + end) // 2

        if list_size == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        while(nums[cur] != target):
            if end - start == 1:
                return -1
            
            if nums[cur] > target:
                end = cur
                cur = (start + end) // 2
                
            elif nums[cur] < target:
                start = cur
                cur = (start + end) // 2

        return cur