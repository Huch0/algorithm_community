# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node) :
            if not node : return -1

            left = depth(node.left)
            right = depth(node.right)

            return max(left,right)+1

        def dfs(node) :
            if not node : return True

            if not dfs(node.left) : return False
            if not dfs(node.right) : return False

            left = depth(node.left)
            right = depth(node.right)

            if abs(left-right) <= 1 : return True
            else : return False

        return dfs(root)