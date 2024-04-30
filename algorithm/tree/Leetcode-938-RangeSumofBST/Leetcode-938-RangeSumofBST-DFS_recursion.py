# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node) :
            if not node : return 0

            if node.val < low : 
                return dfs(node.right)
            if node.val > high : 
                return dfs(node.left)

            return node.val + dfs(node.right) + dfs(node.left)

        return dfs(root)