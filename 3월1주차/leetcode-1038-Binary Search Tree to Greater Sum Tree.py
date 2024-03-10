# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        dq = collections.deque([root]) # bfs방식으로 tree를 array로 변환
        array = []
        while dq:
            for i in range(len(dq)):
                if dq[0] == None:
                    array.append(dq.popleft())
                else:
                    array.append(dq[0].val)
                    dq.append(dq[0].left)
                    dq.append(dq[0].right)
                    dq.popleft()
        
        modified = collections.deque(array)
        for i in range(len(array)):
            if array[i] == None:
                continue
            for j in range(len(array)):
                if array[j] == None:
                    continue
                if array[i] > array[j]:
                    modified[j] = modified[j] + array[i]

        dq = collections.deque([root])
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if not node:
                    modified.popleft()
                else:
                    node.val = modified.popleft()
                    dq.append(node.left)
                    dq.append(node.right)
        return root