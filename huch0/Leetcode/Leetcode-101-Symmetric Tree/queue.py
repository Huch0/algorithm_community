# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False

        q = collections.deque()
        q.append((root.left, root.right))
        while q:
            l, r = q.popleft()

            if (l is not None and r is None) or (l is None and r is not None):
                return False
            elif l is None and r is None:
                continue

            if l.val != r.val:
                return False

            q.append((l.left, r.right))
            q.append((l.right, r.left))

        return True
