class Solution(object):
    def productExceptSelf(self, nums):
        num = [] #if num = [1,2,3,4]
        a = 1
        for i in range(0,len(nums)):
            num.append(a)
            a = a * nums[i] #p = 1 1 2 6, num = 1 1 2 6
        
        a = 1
        for i in range(len(nums)-1, -1, -1):
            num[i] = num[i] * a
            a = a * nums[i]
    
        return num
