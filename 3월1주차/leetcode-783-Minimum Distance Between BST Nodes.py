# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        myarray = []
        dq = collections.deque([root])
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node:
                    myarray.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
        myarray.sort()
        
        answer = myarray[1] - myarray[0]
        for i in range(1, len(myarray) - 1):
            answer = min(myarray[i+1] - myarray[i], answer)
        return answer