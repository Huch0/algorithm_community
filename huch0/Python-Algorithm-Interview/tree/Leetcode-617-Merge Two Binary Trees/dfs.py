# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        merged = TreeNode()

        def dfs(cur_merged: TreeNode, cur1: TreeNode, cur2: TreeNode):
            # Sum cur1.val and cur2.val as the new value of the cur_merged
            cur_merged.val = cur1.val + cur2.val

            # There is at least one node on the lefthand side
            if cur1.left or cur2.left:
                cur_merged.left = TreeNode()

                # Create new node with value 0 if there is no Node in a tree.
                if not cur1.left:
                    cur1.left = TreeNode()
                if not cur2.left:
                    cur2.left = TreeNode()

                dfs(cur_merged.left, cur1.left, cur2.left)

            # There is at least one node on the righthand side
            if cur1.right or cur2.right:
                cur_merged.right = TreeNode()

                # Create new node with value 0 if there is no Node in a tree.
                if not cur1.right:
                    cur1.right = TreeNode()
                if not cur2.right:
                    cur2.right = TreeNode()

                dfs(cur_merged.right, cur1.right, cur2.right)

        if not root1 and not root2:
            return None

        if not root1:
            root1 = TreeNode()
        if not root2:
            root2 = TreeNode()

        dfs(merged, root1, root2)

        return merged
