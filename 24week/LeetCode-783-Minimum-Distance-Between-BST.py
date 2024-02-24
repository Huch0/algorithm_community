# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        stack = [root]
        visited = set()
        prev_node = None
        min_diff = 100000

        while stack:
            current_node = stack[-1]
            if current_node.left and current_node.left not in visited:
                stack.append(current_node.left)
                continue

            if prev_node:
                if current_node.val - prev_node.val < min_diff:
                    min_diff = current_node.val - prev_node.val

            prev_node = stack.pop()
            visited.add(prev_node)

            if current_node.right:
                stack.append(current_node.right)

        return min_diff