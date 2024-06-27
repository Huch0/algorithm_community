import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)

        for i in dic.keys() :
           if dic[i] == 1 : return i

        