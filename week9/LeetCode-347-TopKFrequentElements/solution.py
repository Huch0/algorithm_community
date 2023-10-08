class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = set(nums)
        counter = {}
        for key in keys:
            counter[key] = 0
            
        for num in nums:
            counter[num] += 1
        
        sorted_counter = sorted(counter.values())
        return [sorted_counter[i] for i in range(k)]