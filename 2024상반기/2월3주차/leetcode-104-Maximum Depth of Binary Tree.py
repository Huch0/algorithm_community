# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #  dfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getheight(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            else:
                return max(getheight(node.left) + 1, getheight(node.right) + 1)
        return getheight(root)
    
class Solution: # bfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        dq = collections.deque([root])
        answer = 0
        while dq:
            answer = answer + 1
            for i in range(len(dq)):
                cur = dq.popleft()
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
        return answer