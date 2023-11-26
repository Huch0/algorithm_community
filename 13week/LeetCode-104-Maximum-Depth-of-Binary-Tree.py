# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: list[TreeNode]) -> int:
        def depth(node):
            if node is None:
                return 0
            return max(depth(node.left), depth(node.right))+1
        
        return depth(root)