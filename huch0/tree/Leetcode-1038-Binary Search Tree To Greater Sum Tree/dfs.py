# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global_sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def right_traversal(cur: TreeNode):
            # Traverse right first to reach the largest node.
            if cur.right:
                right_traversal(cur.right)

            # Current Node Action : add val to global_sum and re-asign val
            self.global_sum += cur.val
            cur.val = self.global_sum

            if cur.left:
                right_traversal(cur.left)

        right_traversal(root)

        return root
