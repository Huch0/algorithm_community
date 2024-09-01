# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightside_nodes = []

        queue = collections.deque([(root, 0)])
        while queue:
            cur, level = queue.popleft()
            if not cur:
                continue

            if level == len(rightside_nodes):
                rightside_nodes.append(cur.val)

            queue.append((cur.right, level + 1))
            queue.append((cur.left, level + 1))

        return rightside_nodes
