# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # A nested function can read variables of parent.
    # However, if a nested function re-align the value of variable of parent,
    # it defined as a local variable of nested function with a different reference ID.

    # So, I defined max_path as a class variable so that dfs and logenstUnivaluePath can align values to it freely
    max_path: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(cur: TreeNode) -> int:
            # These heights are for tracking 'univalue' height.
            l_h = r_h = 0

            left, right = cur.left, cur.right

            if left:
                if left.val == cur.val:
                    l_h = dfs(left) + 1
                else:  # if a child has different value, this side of univalue height is 0.
                    dfs(left)

            if right:
                if right.val == cur.val:
                    r_h = dfs(right) + 1
                else:
                    dfs(right)

            # Current subtree's maximum univalue path is l_h + r_h
            # Update maximum univalue path
            self.max_path = max(self.max_path, l_h + r_h)

            # Return current node's univalue height.
            return max(l_h, r_h)

        if not root:
            return 0

        dfs(root)

        return self.max_path
