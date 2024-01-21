# dfs(using recursion)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(List,index) :
            if len(List) == len(nums) :
                return
            
            for i in range(index, len(nums)) :
                List.append(nums[i])
                result.append(List[:])
                dfs(List,i+1)
                List.pop()
            
            return

        result = [[]]
        dfs([],0)

        
        return result