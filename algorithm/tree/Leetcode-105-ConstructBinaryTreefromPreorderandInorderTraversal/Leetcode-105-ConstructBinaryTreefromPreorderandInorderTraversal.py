# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder and inorder :
            tree = TreeNode(preorder.pop(0))
            
            root_index = inorder.index(tree.val)

            tree.left = self.buildTree(preorder[:root_index], inorder[:root_index])
            tree.right = self.buildTree(preorder[root_index:], inorder[root_index+1:])

            return tree