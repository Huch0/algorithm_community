# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    min_diff = 100000
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root : return self.min_diff
        
        print(root.val)

        if root.left :
            left_compare_node = root.left
            while left_compare_node.right :
                left_compare_node = left_compare_node.right
            self.min_diff = min(self.min_diff,abs(root.val-left_compare_node.val))


        if root.right :
            right_compare_node = root.right
            while right_compare_node.left :
                right_compare_node = right_compare_node.left
            self.min_diff = min(self.min_diff,abs(root.val-right_compare_node.val))

        self.minDiffInBST(root.left)
        self.minDiffInBST(root.right)

        return self.min_diff
