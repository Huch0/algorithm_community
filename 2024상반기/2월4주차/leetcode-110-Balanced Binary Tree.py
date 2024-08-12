# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 내 풀이
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        unbalanceFlag = 0
        def dfs(node): # 자신을 root로 했을 때 tree의 깊이를 return함. None이면 0, 자기만 있으면 1, ..
            nonlocal unbalanceFlag
            if not node or unbalanceFlag:
                return 0

            ld, rd = dfs(node.left), dfs(node.right)
            if abs(ld-rd) > 1:
                unbalanceFlag = 1
                return 0
            return max(ld, rd) + 1

        dfs(root)
        if unbalanceFlag:
            return False
        else:
            return True
        
class Solution: # 솔루션 : unbalancedFlag 대신 dfs함수가 -1을 return하면 불균형한 것으로 약속
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node): # 자신을 root로 했을 때 tree의 깊이를 return함. None이면 0, 자기만 있으면 1, ..
            if not node:
                return 0

            ld, rd = dfs(node.left), dfs(node.right)
            if ld == -1 or rd == -1 or abs(ld-rd) > 1:
                return -1

            return max(ld, rd) + 1

        if dfs(root) == -1:
            return False
        else:
            return True