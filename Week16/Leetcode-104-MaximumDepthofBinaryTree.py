# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None : return 0

        queue = collections.deque([root])

        depth = 0
        while queue :
            depth += 1

            for _ in range(len(queue)):
                pop = queue.popleft()

                if pop.left :
                    queue.append(pop.left)
                if pop.right :
                    queue.append(pop.right)
        
        return depth