# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cur_max = -float('inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if self.cur_max >= root.val:
            return False

        self.cur_max = root.val

        if not self.isValidBST(root.right):
            return False

        return True
