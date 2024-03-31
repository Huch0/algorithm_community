# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # Divide inorder result by preorder result
            pivot = inorder.index(preorder.pop(0))

            # Pivot(First element of preorder) is root of subtree
            root = TreeNode(inorder[pivot])

            # Conquer left and right side of inorder result.
            # each side of pivot is left/right subtree.
            root.left = self.buildTree(preorder, inorder[:pivot])
            root.right = self.buildTree(preorder, inorder[pivot + 1:])

            return root
