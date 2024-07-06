class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        current_max = float('-inf')

        for i in range(len(nums)) :
            window.append(nums[i])
        
            if i < k-1 : 
                continue 

            if current_max == float('-inf') :
                current_max = max(window)
            elif nums[i] > current_max :
                current_max = nums[i]
            
            result.append(current_max)

            if current_max == window.popleft() :
                current_max = float('-inf')
        
        return result