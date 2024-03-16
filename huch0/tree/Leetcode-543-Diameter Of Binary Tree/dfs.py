# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(cur_root: TreeNode, max_diameter: int) -> int:
            left, right = cur_root.left, cur_root.right

            # Base Case : Leaf Node has height 0
            if not left and not right:
                return 0

            l_height = r_height = 0

            if left:
                l_height = dfs(left, max_diameter) + 1
            if right:
                r_height = dfs(right, max_diameter) + 1

            # cur_diameter is equals to the sum of the diameters of left subtree and right subtree
            cur_diameter = l_height + r_height

            # Update max_diameter if cur_diameter is larger
            max_diameter[0] = max(max_diameter[0], cur_diameter)

            # The height of current root
            height = max(l_height, r_height)

            return height

        # Int is immutable, so define as list to make it mutable
        max_diameter = [0]

        dfs(root, max_diameter)

        return max_diameter[0]
