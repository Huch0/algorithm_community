class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def permutation(li):
            if len(li) == len(nums):
                answer.append(li[:])
                return
            for n in nums:
                if n not in li:
                    li.append(n)
                    permutation(li)
                    li.pop()
        permutation([])
        return answer