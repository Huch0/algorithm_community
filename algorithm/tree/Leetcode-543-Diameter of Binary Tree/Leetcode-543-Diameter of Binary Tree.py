# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # use class variable to reallocation in the 'dfs' function
    longest_distance = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node) :
            # if the end is exceeded, '-1' is returned to signal the end
            if not node : return -1
            
            # distance to the left/right leaf node (state value)
            left = dfs(node.left)
            right = dfs(node.right)

            distance = left + right + 2

            if self.longest_distance < distance : self.longest_distance = distance

            # return state value
            return max(left,right)+1
        
        dfs(root)

        return self.longest_distance
