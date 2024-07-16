# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        global_level = 0
        level_nodes = []
        q = collections.deque()
        q.append((0, root))
        while q:
            level, node = q.popleft()

            if level != global_level:
                ans.append(level_nodes)
                global_level += 1
                level_nodes = []

            if not node:
                continue

            level_nodes.append(node.val)

            q.append((level + 1, node.left))
            q.append((level + 1, node.right))

        return ans
