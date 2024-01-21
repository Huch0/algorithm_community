# dfs(using recursion)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(List,index) :
            if sum(List) == target : 
                result.append(List[:])
                return
            elif sum(List) > target :
                return
            
            for i in range(index,len(candidates)) :
                List.append(candidates[i])
                dfs(List,i)
                List.pop()
            
        result = []
        dfs([],0)

        return result

            
        