# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(cur: TreeNode):
            # Swap left and right
            cur.left, cur.right = cur.right, cur.left

            # Call Recursively
            if cur.left:
                dfs(cur.left)
            if cur.right:
                dfs(cur.right)

        if not root:
            return None

        dfs(root)

        return root
