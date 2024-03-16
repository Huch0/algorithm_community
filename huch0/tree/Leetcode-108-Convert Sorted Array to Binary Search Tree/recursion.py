# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        median = len(nums) // 2

        node = TreeNode(nums[median])
        node.left = self.sortedArrayToBST(nums[:median])
        node.right = self.sortedArrayToBST(nums[median + 1:])

        return node
