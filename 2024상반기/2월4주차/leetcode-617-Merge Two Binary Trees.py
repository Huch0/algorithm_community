# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 내 풀이
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None:
            return root2
        if root2 == None:
            return root1

        def dfs(node1, node2): # node1에다가 node2를 더해주는 느낌. node2가 있으니까 온거야. 없으면 올 필요가 없음.
            node1.val = node1.val + node2.val
            if node2.left:
                if node1.left:
                    dfs(node1.left, node2.left)
                else:
                    node1.left = node2.left
            if node2.right:
                if node1.right:
                    dfs(node1.right, node2.right)
                else:
                    node1.right = node2.right
        dfs(root1, root2)
        return root1

class Solution: # 솔루션 - mergeTrees함수 자체를 재귀로 만듬
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:
            return root1 or root2 ## 이런식으로 return하는거 처음봄