# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = collections.deque([root])
        sum_of_node = 0

        while queue :
            node = queue.popleft()

            if not node : continue

            if node.val < low : queue.append(node.right)
            elif node.val > high : queue.append(node.left)
            else : 
                sum_of_node += node.val
                queue.append(node.left)
                queue.append(node.right)
        return sum_of_node
            
            