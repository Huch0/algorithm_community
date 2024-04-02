# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node) :
            if not node : return

            if node.left and not node.right :
                node.right = node.left
                node.left = None
                dfs(node.right)
                return
            elif node.right and not node.left :
                node.left = node.right
                node.right = None
                dfs(node.left)
                return
            elif node.right and node.left :
                node.left, node.right = node.right, node.left
                dfs(node.left)
                dfs(node.right)
                return
            else : return
            
        dfs(root)
        return root