class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        
        nums = [num for num in range(1,n+1)]

        prev_elements = []
        #dfs 구현
        def dfs(nums, start, k):
            if k == 0:
                result.append(prev_elements[:])
                return
            for i in range(start, len(nums)):
                prev_elements.append(nums[i])
                dfs(nums, i+1, k-1)
                prev_elements.pop()
            
        #dfs 호출
        dfs(nums, 0, k)

        #dfs 결과 반환
        return result
    
        #return list(itertools.combinations(nums, k)) #itertools 사용한 풀이
        