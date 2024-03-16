# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur: TreeNode) -> int:
            l_depth = r_depth = 0

            if cur.left:
                l_depth = dfs(cur.left)
            if cur.right:
                r_depth = dfs(cur.right)

            if l_depth == -1 or r_depth == -1:
                return -1

            if abs(l_depth - r_depth) > 1:
                return -1

            return max(l_depth, r_depth) + 1

        if not root:
            return 1

        return dfs(root) != -1
