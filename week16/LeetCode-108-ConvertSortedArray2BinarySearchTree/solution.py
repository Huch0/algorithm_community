# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def BST(nodes: List[int]) -> TreeNode:
            if not nodes:
                return None
            
            root_index = len(nodes) // 2
            root = TreeNode(nodes[root_index])
            root.left = BST(nodes[:root_index])
            root.right = BST(nodes[root_index + 1:])

            return root
        
        result = BST(nums)

        return result
        