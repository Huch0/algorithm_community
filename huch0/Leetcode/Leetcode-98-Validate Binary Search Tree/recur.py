# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def minmax(root):
            if not root:
                return [None, None]

            lmin, lmax = minmax(root.left)
            rmin, rmax = minmax(root.right)
            print(lmin, lmax, root.val, rmin, rmax)

            if (lmax is not None and lmax >= root.val) or (rmin is not None and root.val >= rmin):
                raise Exception

            if not lmin:
                lmin = root.val
            if not rmax:
                rmax = root.val

            return [lmin, rmax]

        try:
            minmax(root)
        except:
            return False

        return True
