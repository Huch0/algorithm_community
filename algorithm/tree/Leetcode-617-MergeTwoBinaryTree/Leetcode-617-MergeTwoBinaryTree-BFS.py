# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 : return root2
        if not root2 : return root1
        
        queue1 = collections.deque([root1])
        queue2 = collections.deque([root2])

        while queue1 or queue2 :
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            node1.val = node1.val + node2.val

            if node1.left :
                if node2.left :
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                else : 
                    pass
            else :
                if node2.left :
                    node1.left = node2.left
                else : pass

            if node1.right :
                if node2.right :
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                else : 
                    pass
            else :
                if node2.right :
                    node1.right = node2.right
                else : pass

            
        return root1
            

        


        