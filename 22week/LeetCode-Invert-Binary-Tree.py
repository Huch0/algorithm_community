# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        def dfs(start):
            stack = [start]
        
            while stack:
                cur_node = stack.pop()
                if cur_node.left:
                    stack.append(cur_node.left)
                if cur_node.right:
                    stack.append(cur_node.right)

                cur_node.left, cur_node.right = cur_node.right, cur_node.left

        dfs(root)

        return root