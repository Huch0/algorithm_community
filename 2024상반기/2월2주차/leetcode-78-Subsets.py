class Solution: # 내 풀이 - 부분집합의 원소의 갯수에 따라 분류해서 생각
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        subset = []
        def recursive(curIndex, setSize):
            if len(subset) == setSize:
                answer.append(subset[:])
                return
            for i in range(curIndex, len(nums)):
                subset.append(nums[i])
                recursive(i+1, setSize)
                subset.pop()
        for i in range(0, len(nums)+1):
            recursive(0, i)
        return answer
    
class Solution: # 솔루션 - 가능한 모든 경우의 수를 dfs로 찾아서 추가하기
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(index, subset):
            answer.append(subset[:])
            for i in range(index, len(nums)):
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop()
        
        dfs(0, [])
        return answer