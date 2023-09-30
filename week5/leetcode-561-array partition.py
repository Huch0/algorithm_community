class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
#슬라이싱이랑 range랑 비슷함
#range(a,b) = array[a:b]
#range(a,b,c) = array[a:b:c]


#처음풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            answer += nums[i]
        return answer