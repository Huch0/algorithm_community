# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0
        def dfs(node):
            nonlocal answer
            if low <= node.val <= high:
                answer = answer + node.val
            if node.left and node.val > low:
                dfs(node.left)
            if node.right and node.val < high:
                dfs(node.right)
        dfs(root)
        return answer