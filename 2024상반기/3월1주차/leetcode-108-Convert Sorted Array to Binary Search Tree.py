# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bfs(array, node, lr): # lr이 0이면 node의 왼쪽, 1이면 오른쪽에 붙인다
            if len(array) == 0:
                return
            l = len(array)
            l = l//2
            if lr == 0:
                node.left = TreeNode(array[l])
                bfs(array[:l], node.left, 0)
                bfs(array[l+1:], node.left, 1)
            else:
                node.right = TreeNode(array[l])
                bfs(array[:l], node.right, 0)
                bfs(array[l+1:], node.right, 1)
        root = TreeNode(0)
        bfs(nums, root, 0)
        return root.left

class Solution: # 솔루션을 참고한 좀 더 깔끔한 재귀 코드
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        l = len(nums) // 2
        node = TreeNode(nums[l])
        node.left = self.sortedArrayToBST(nums[:l])
        node.right = self.sortedArrayToBST(nums[l+1:])
        return node