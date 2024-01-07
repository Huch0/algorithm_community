# first commit ( Add the key and value of the counter to the tuple list and output k elements after sorting. )
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        tuple_list = []
        result = []

        for char in counter.keys() :
            tuple_list.append((counter[char],char))
        tuple_list.sort(reverse=True)

        for i in range(k) :
            result.append(tuple_list[i][1])
        
        return result
    
"""
using heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        counter_heap = []
        for c in counter :
            heapq.heappush(counter_heap,(-counter[c],c))
        
        result = []
        for i in range(k) :
            result.append(heapq.heappop(counter_heap)[1])
        return result 
"""