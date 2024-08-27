# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            cur, depth = stack.pop()
            if not cur:
                max_depth = max(max_depth, depth - 1)
                continue

            stack.append((cur.left, depth + 1))
            stack.append((cur.right, depth + 1))

        return max_depth
