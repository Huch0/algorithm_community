# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        #compute left height tree
        left = self.isBalanced(root.left)
        if left == 0:
            return 0
        right = self.isBalanced(root.right)
        if right == 0:
            return 0
        if (abs(left-right) > 1):
            return 0
        else:
            return max(left, right) +1