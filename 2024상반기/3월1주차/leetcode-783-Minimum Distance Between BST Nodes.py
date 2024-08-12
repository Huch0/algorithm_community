# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # array로 바꿔서 sort하기
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

class Solution: # BST의 특징 이용해서 dfs함수 만들기
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        answer = 100001
        def dfs(node):
            nonlocal answer
            if node.left:
                leftMaxNode = node.left
                while True:
                    if leftMaxNode.right:
                        leftMaxNode = leftMaxNode.right
                    else:
                        leftMax = leftMaxNode.val
                        break
                answer = min(answer, node.val - leftMax)
                dfs(node.left)
            if node.right:
                rightMinNode = node.right
                while True:
                    if rightMinNode.left:
                        rightMinNode = rightMinNode.left
                    else:
                        rightMin = rightMinNode.val
                        break
                answer = min(answer, rightMin - node.val)
                dfs(node.right)
        dfs(root)
        return answer
class Solution: # dfs함수가 뭔가 리턴하는 방식으로 짜고싶어서 살짝 수정
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            answer = 100001
            if node.left:
                leftMaxNode = node.left
                while True:
                    if leftMaxNode.right:
                        leftMaxNode = leftMaxNode.right
                    else:
                        leftMax = leftMaxNode.val
                        break
                answer = node.val - leftMax
                answer = min(answer, dfs(node.left))
            if node.right:
                rightMinNode = node.right
                while True:
                    if rightMinNode.left:
                        rightMinNode = rightMinNode.left
                    else:
                        rightMin = rightMinNode.val
                        break
                answer = min(answer, rightMin - node.val)
                answer = min(answer, dfs(node.right))
            return answer
        
        return dfs(root)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 중위 순회 이용하기 (문제에 딱 맞는 순회 방법임)
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        answer = sys.maxsize
        prev = -sys.maxsize

        def round(node):
            nonlocal answer
            nonlocal prev

            if node.left:
                round(node.left)
            answer = min(answer, node.val - prev)
            prev = node.val
            if node.right:
                round(node.right)
        
        round(root)
        return answer