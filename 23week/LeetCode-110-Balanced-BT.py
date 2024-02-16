# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# save Left_height, Right_Height of All_node with DFS
# if any node are exist such that abs(Left_height - Right_Height) > 1 -> False
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def dfs_height(start):
            result = []
            max_distance = 0
            if start.left:
                stack = [(start.left, 1)]
                while stack:
                    cur_node, distance = stack.pop()  # 스택에서 노드와 해당 노드의 깊이를 가져옴
                    max_distance = max(max_distance, distance)  # 최대 깊이 업데이트
                    # 왼쪽 자식이 있으면 스택에 추가
                    if cur_node.left:
                        stack.append((cur_node.left, distance + 1))
                    # 오른쪽 자식이 있으면 스택에 추가
                    if cur_node.right:
                        stack.append((cur_node.right, distance + 1))
            
            result.append(max_distance)

            max_distance = 0
            if start.right:
                stack = [(start.right, 1)]
                while stack:
                    cur_node, distance = stack.pop()  # 스택에서 노드와 해당 노드의 깊이를 가져옴
                    max_distance = max(max_distance, distance)  # 최대 깊이 업데이트
                    # 왼쪽 자식이 있으면 스택에 추가
                    if cur_node.left:
                        stack.append((cur_node.left, distance + 1))
                    # 오른쪽 자식이 있으면 스택에 추가
                    if cur_node.right:
                        stack.append((cur_node.right, distance + 1))
            
            result.append(max_distance)

            return result
        
        def dfs(start):
            stack = [start]

            while stack:
                cur_node = stack.pop()
                node_height = dfs_height(cur_node)
                
                if abs(node_height[1]- node_height[0]) > 1:
                    return False
                if cur_node.left:
                    stack.append(cur_node.left)
                # 오른쪽 자식이 있으면 스택에 추가
                if cur_node.right:
                    stack.append(cur_node.right)

                print(f"{cur_node.val}, |{node_height[0]}, {node_height[1]}|")
            
            return True
        
        if not dfs(root):
            return False
        return True
    
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, False)]
        heights = {}
        balanced = True

        while stack:
            node, visited = stack.pop()

            if visited:
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)
                if abs(left_height - right_height) > 1:
                    balanced = False
                    break
                heights[node] = max(left_height, right_height) + 1
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return balanced

"""