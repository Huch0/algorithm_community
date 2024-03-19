class Solution:
    def topKFrequent(self, nums, k):
        freq={}

        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        sort_freq=[(val,key) for key, val in freq.items()]
        sort_freq.sort(reverse=True)

        ans=[val for key, val in sort_freq[:k]]

        return ans
       