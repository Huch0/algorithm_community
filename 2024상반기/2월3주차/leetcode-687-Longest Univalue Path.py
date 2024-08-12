# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node): # 리턴할 값은 편도로 얼마나 긴가 / answer에 넣을 때는 왼쪽과 오른쪽의 길이를 더한것과 비교해서 넣어준다
            if not node:
                return 0
            leftlength = dfs(node.left)
            rightlength = dfs(node.right)
            curlength = 0
            toreturn = 0
            if node.left and node.left.val == node.val:
                curlength = curlength + leftlength + 1
                toreturn = leftlength + 1
            if node.right and node.right.val == node.val:
                curlength = curlength + rightlength + 1
                toreturn = max(toreturn, rightlength + 1)
            nonlocal answer
            if curlength > answer:
                answer = curlength
            return toreturn
            
        dfs(root)
        return answer