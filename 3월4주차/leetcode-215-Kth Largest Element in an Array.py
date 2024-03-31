class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myheap = []
        for n in nums:
            heapq.heappush(myheap, -n)
        for i in range(k-1):
            heapq.heappop(myheap)
        return -heapq.heappop(myheap)