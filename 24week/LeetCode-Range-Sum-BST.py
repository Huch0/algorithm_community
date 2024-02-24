# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        sum = 0
        
        while stack:
            current_node = stack.pop()
            if current_node.val >= low and current_node.val <= high:
                sum += current_node.val

                # 범위의 왼쪽 끝 값인 경우
                if current_node.val == low:
                    if current_node.right:
                        stack.append(current_node.right)
                
                # 범위의 오른쪽 끝 값인 경우
                elif current_node.val == high:
                    if current_node.left:
                        stack.append(current_node.left)
                
                # 범위 내부의 값인 경우
                else:
                    if current_node.left:
                        stack.append(current_node.left)
                    if current_node.right:
                        stack.append(current_node.right)
  
            elif current_node.val < low:
                if current_node.right:
                    stack.append(current_node.right)
            
            elif current_node.val > high:
                if current_node.left:
                    stack.append(current_node.left)

        return sum