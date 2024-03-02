class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find pivot index
        def isPivotHere(interval: List[int]) -> bool:
            if not interval:
                return False  # Empty list is not a valid pivot
            return interval[0] > interval[-1]
        
        def findTarget(start: int, end: int) -> int:
            
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        pivot = 0
        if nums[0] < nums[-1] or len(nums) == 1:
            return findTarget(0, len(nums) - 1)
        else:
            #find pivot
            start, end = 0, len(nums) - 1
            pivotFound = False

            while not pivotFound:
                pivot = (start + end) // 2
                print(pivot)
                if (not isPivotHere(nums[:pivot]) and not isPivotHere(nums[pivot:])):
                    if nums[pivot] == nums[pivot - 1]:
                        pivot = 0
                    pivotFound = True
                elif isPivotHere(nums[:pivot]):
                    end = pivot - 1 
                else:
                    start = pivot + 1 
            #and find target
            if target > nums[0]:
                return findTarget(0, pivot)
            elif target < nums[0]:
                return findTarget(pivot, len(nums) - 1)
            else:
                return 0