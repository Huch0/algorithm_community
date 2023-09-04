class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        # L[i] contains the product of all the numbers to the left of i
        L = [0]*length 
        L[0] = 1
        
        # R[i] contains the product of all the numbers to the right of i
        R = [0]*length 
        R[length - 1] = 1

        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]

        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]

        # Construct the answer array
        answer = [L[i]*R[i] for i in range(length)]
        
        return answer
