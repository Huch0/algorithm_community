# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []

        def inorder_traversal(cur):
            if not cur:
                return

            inorder_traversal(cur.left)
            nodes.append(cur.val)
            inorder_traversal(cur.right)

        inorder_traversal(root)
        print(nodes)
        return nodes[k - 1]
