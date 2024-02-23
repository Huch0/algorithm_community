# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = [root]
        inheritance = 0

        visited = set()

        while stack:
            current_node = stack[-1]
            if current_node.right and current_node.right not in visited:
                stack.append(current_node.right)
                continue

            visited.add(current_node)
            
            inheritance += current_node.val
            current_node.val = inheritance

            stack.pop()

            if current_node.left:
                stack.append(current_node.left)

        return root