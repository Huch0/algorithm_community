# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_of_node = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        discovered = set()
        def dfs(node) :
            if not node : return 

            dfs(node.right)
            if node.val not in discovered :
                discovered.add(node.val)
                self.sum_of_node += node.val
                node.val = self.sum_of_node
                discovered.add(node.val)
            else : pass
            dfs(node.left)

            return
        dfs(root)
        return root
