# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(cur):
            if not cur:
                return None, None

            # Divde and Conquer
            l_start, l_end = flat(cur.left)
            r_start, r_end = flat(cur.right)
            cur.left, cur.right = None, None

            # Merge
            if l_start:
                cur.right = l_start
                if r_start:
                    l_end.right = r_start
                    return cur, r_end
                else:
                    return cur, l_end
            else:
                if r_start:
                    cur.right = r_start
                    return cur, r_end
                else:  # Both childs are None
                    return cur, cur

        flat(root)
