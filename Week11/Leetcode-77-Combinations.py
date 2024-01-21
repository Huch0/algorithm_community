# dfs(using recursion)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(List,todo) :
            if (len(List) == k) :
                result.append(List[:])
                return
            
            for i in range(len(todo)) :
                List.append(todo[i])
                new_todo = todo[i+1:]

                dfs(List,new_todo)
                List.pop()
        
        result = []
        dfs([],list(range(1,n+1)))

        return result
    