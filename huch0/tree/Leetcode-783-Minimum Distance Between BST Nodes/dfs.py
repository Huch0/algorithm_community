# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global_min_diff = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(cur: TreeNode) -> (int, int):
            # Handle leaves (None Type)
            if not cur:
                # Return invalid values because (0 <= Node.val <= 105)
                return (-1, -1)

            sub_min = sub_max = cur.val
            ld = rd = sys.maxsize  # Invalid differences won't affect global_min_diff

            left_tuple = dfs(cur.left)
            right_tuple = dfs(cur.right)

            # Check is tuple invalid
            if left_tuple[0] != -1:
                ld = cur.val - left_tuple[1]
                sub_min = left_tuple[0]

            if right_tuple[0] != -1:
                rd = right_tuple[0] - cur.val
                sub_max = right_tuple[1]

            # Update global_min_diff
            sub_min_diff = min(ld, rd)
            self.global_min_diff = min(self.global_min_diff, sub_min_diff)

            return (sub_min, sub_max)

        dfs(root)

        return self.global_min_diff
