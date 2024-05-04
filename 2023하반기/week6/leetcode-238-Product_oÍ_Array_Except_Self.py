class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        n = 1
        for k in nums[:-1]:
            n *= k
            answer.append(n)
        n = 1
        for i in range(len(nums)-2, -1, -1):
            n *= nums[i+1]
            answer[i] *= n
        return answer

#똑같은 코드인데 insert로 하니까 엄청느림 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        right = [nums[-1]]
        for n in nums[1:]:
            left.append(n*left[-1])
        for i in range(len(nums)-2, -1, -1):
            right.append(nums[i]*right[-1])
        answer = [right[-2]]
        for i in range(1, len(nums)-1):
            answer.append(left[i-1]*right[len(nums)-i-2])
        answer.append(left[-2])
        return answer
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        right = [nums[-1]]
        for n in nums[1:]:
            left.append(n*left[-1])
        for i in range(len(nums)-2, -1, -1):
            right.insert(0, nums[i]*right[0])
        answer = [right[1]]
        for i in range(1, len(nums)-1):
            answer.append(left[i-1]*right[i+1])
        answer.append(left[-2])
        return answer