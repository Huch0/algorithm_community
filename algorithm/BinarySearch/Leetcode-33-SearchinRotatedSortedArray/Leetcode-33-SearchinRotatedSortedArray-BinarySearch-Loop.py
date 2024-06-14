class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] : 
                start = i+1
                break

        left = start
        right = len(nums)-1
        while True :
            if left > right : break
            mid = left + (right-left)//2 
            if nums[mid] > target :
                right = mid-1
            elif nums[mid] < target :
                left = mid+1
            else : return mid

        left = 0
        right = start-1
        while True :
            if left > right : break
            mid = left + (right-left)//2 
            if nums[mid] > target :
                right = mid-1
            elif nums[mid] < target :
                left = mid+1
            else : return mid
        return -1