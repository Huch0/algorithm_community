class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []  # List to store maximum values
        q = deque()  # Deque to hold indices of nums

        for i, n in enumerate(nums):
            # Remove indices that are out of the current window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove indices of elements smaller than the current element
            while q and nums[q[-1]] <= n:
                q.pop()

            q.append(i)  # Add the current index to the deque

            if i >= k - 1:
                # The leftmost index in the deque contains the maximum
                ans.append(nums[q[0]])

        return ans
