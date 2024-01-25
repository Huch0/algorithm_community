# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum_node = 0
        def GST(node : TreeNode) -> int:
            if not node:
                return 0
            nonlocal sum_node
            GST(node.right)
            node.val += sum_node
            sum_node = node.val
            GST(node.left)
            return node.val

        GST(root)
        return root