class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
            if i in list(count.keys()):
                count[i] += 1
            else: 
                count[i] = 1
        
        res = [i[0] for i in count.items() if i[1] > len(nums)/2]
        return res[0]