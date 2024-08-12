# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # bfs
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = collections.deque([root])
        while dq:
            for i in range(len(dq)):
                curnode = dq.popleft()
                if not curnode:
                    continue
                curnode.left, curnode.right = curnode.right, curnode.left
                dq.append(curnode.left)
                dq.append(curnode.right)
        return root
    
class Solution: # dfs
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # 자식이 서로 바뀐 root를 리턴하는 재귀함수
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        else:
            return None