# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev_val = -sys.maxsize
    min_diff = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        # Inorder Traversal to calculate differences
        # 1. cur.val - max value of the left sub tree
        # 2. min value of the right sub tree - cur.val
        self.min_diff = min(self.min_diff, root.val - self.prev_val)
        self.prev_val = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.min_diff
