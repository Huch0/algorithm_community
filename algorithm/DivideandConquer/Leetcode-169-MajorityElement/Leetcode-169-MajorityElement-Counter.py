import collections

def majorityElement(nums: list[int]) -> int: 
    counter = collections.Counter(nums)
    for i in counter.keys() :
        if counter[i] > len(nums)//2 :
            return i
        
print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))