# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder.reverse()
        inorderDict = { v:i for i,v in enumerate(inorder) }
        return self.buildTreeHelper(preorder, inorderDict, 0, len(preorder) - 1)
    def buildTreeHelper(self, preorder, inorderDict, beg, end):
        if beg > end: return None
        root = TreeNode(preorder.pop())
        index = inorderDict[root.val]
        
        root.left = self.buildTreeHelper(preorder, inorderDict, beg, index - 1)
        root.right = self.buildTreeHelper(preorder, inorderDict, index + 1, end)
        return root