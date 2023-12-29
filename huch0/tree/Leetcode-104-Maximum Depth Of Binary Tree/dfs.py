# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(cur: TreeNode, depth: int) -> int:
            left_depth = right_depth = depth
            if cur.left:
                left_depth = dfs(cur.left, depth + 1)
            if cur.right:
                right_depth = dfs(cur.right, depth + 1)

            if not cur.left and not cur.right:
                return depth
            else:
                return max(left_depth, right_depth)

        if not root:
            return 0

        return dfs(root, 1)
