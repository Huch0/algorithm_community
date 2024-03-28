# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node) :
            if not node : return -1
            
            if not node.left and not node.right : return 0
            
            elif node.left and not node.right : 
                left = dfs(node.left)

                if node.val == node.left.val :
                    distance = left + 1
                    if self.longest < distance : self.longest = distance
                    return left + 1
                else : return 0
            
            elif node.right and not node.left : 
                right = dfs(node.right)

                if node.val == node.right.val :
                    distance = right + 1
                    if self.longest < distance : self.longest = distance
                    return right + 1
                else : return 0 
            
            else :           
                left = dfs(node.left)
                right = dfs(node.right)

                if node.val == node.left.val and node.val == node.right.val : 
                    distance = left + right + 2
                    if self.longest < distance : self.longest = distance
                    return max(left,right) + 1
                
                elif node.val == node.left.val :
                    distance = left + 1
                    if self.longest < distance : self.longest = distance
                    return left + 1
                
                elif node.val == node.right.val :
                    distance = right + 1
                    if self.longest < distance : self.longest = distance
                    return right + 1
                
                else : return 0
        
        dfs(root)
        return self.longest