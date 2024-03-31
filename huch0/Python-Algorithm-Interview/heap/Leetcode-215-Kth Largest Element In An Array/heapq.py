class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        kth_largest = 0

        for n in nums:
            heapq.heappush(max_heap, -n)

        for _ in range(k):
            kth_largest = - heapq.heappop(max_heap)

        return kth_largest
        # Other solutions :
        # 1. heapq.nlargest
        # return heapq.nlargest(k, nums)[-1]
        # 2. sorted
        # return sorted(nums, reverse=True)[k - 1]
