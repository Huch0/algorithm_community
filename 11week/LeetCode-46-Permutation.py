class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        prev_elements = []
        
        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
                return
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        if not nums:
            return []
        
        dfs(nums)

        return result