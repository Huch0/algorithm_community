# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    in_sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(cur: TreeNode):
            if not cur:
                return
            # Add to sum if in range
            if low <= cur.val <= high:
                self.in_sum += cur.val

            # Don't need to check left if cur.val <= low
            if not cur.val <= low:
                dfs(cur.left)
            # Don't need to check right if cur.val >= high
            if not cur.val >= high:
                dfs(cur.right)

        dfs(root)

        return self.in_sum
