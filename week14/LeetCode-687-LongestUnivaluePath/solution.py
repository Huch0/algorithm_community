# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_len = 0    
        def dfs(prev, root):
            nonlocal max_len
            if not root:
                return 0
            left =  dfs(root, root.left)
            right = dfs(root, root.right)
            max_len = max(max_len, right + left)
            if prev and root.val == prev.val:
                return 1 + max(left, right)
            return 0
        dfs(None, root)
        return max_len
    