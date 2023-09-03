class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        dest = len(nums) - 1

        for i, jump in enumerate(nums):
            if i <= max_jump:
                max_jump = max(max_jump, i + jump)
                if max_jump >= dest:
                    return True

        return False

