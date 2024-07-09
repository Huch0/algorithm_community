# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sol = -1000

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> int:
            if not root:
                return 0

            lsum = max(dfs(root.left), 0)
            rsum = max(dfs(root.right), 0)

            self.sol = max(self.sol, lsum + rsum + root.val)

            return max(lsum, rsum) + root.val

        return max(dfs(root), self.sol)
