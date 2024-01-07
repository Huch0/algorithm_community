class Solution(object):
    def topKFrequent(self, nums, k):
        myDict = {}
        result = []
        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
                
            if myDict[num] == k:
                result.append(num)
            
        return result

#파이썬다운 방식        
# def topKFrequent(self, nums, k):
#         return list(zip(*collections.Counter(nums).most_common(k)))[0]