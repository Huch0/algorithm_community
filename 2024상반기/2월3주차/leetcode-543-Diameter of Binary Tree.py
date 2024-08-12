# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node): # 자신의 높이를 반환 / 모든 노드에 대해 실행되게 해서 답 구하기
            if not node:
                return 0

            leftsubheight = dfs(node.left)
            rightsubheight = dfs(node.right)
            nonlocal answer
            if answer < leftsubheight + rightsubheight:
                answer = leftsubheight + rightsubheight

            if not node.left and not node.right:
                return 1
            else:
                return max(leftsubheight, rightsubheight) + 1

        dfs(root)        
        return answer