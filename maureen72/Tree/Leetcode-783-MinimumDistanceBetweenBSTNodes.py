# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        node = root
        #result = 0

        prev = -sys.maxsize
        result = sys.maxsize

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val
            node = node.right
        
        return result