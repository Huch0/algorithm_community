# Definition for a binary tree node.
# 1. DFS 알고리즘을 사용
# 각 노드의 자식 노드를 방문하면서 값을 비교하고
# 같은 값이면 부모의 count에서 1을 증가한 상태로 visited에 저장
# 다른 값이면 count를 0으로 만들고 stack에 push

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"val: {self.val}"

class Solution:
    def __init__(self):
        self.visited = {}

    def dfs_count(self, start, count, direction = None):
        if not start:
            return 0
        left = 0
        right = 0

        if start.left and start.left.val == start.val:
            left = self.dfs_count(start.left, count+1)

        if start.right and start.right.val == start.val:
            right = self.dfs_count(start.right, count+1)

        if left == 0 and right == 0:
            return count

        if direction == "left":
            return left
        elif direction == "right":
            return right
        else:
            return max(left, right)

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(start):
            stack = [start]
            self.visited[start] = (self.dfs_count(start, 0, "left"), self.dfs_count(start, 0, "right")) 

            while stack:
                cur_node = stack.pop()
                if cur_node.left:
                    stack.append(cur_node.left)
                if cur_node.right:
                    stack.append(cur_node.right)
                self.visited[cur_node] = (self.dfs_count(cur_node, 0, "left"), self.dfs_count(cur_node, 0, "right"))
        
        dfs(root)
        max_element = max(self.visited.values(), key=lambda x: x[0]+x[1])
        
        for k, v in self.visited.items():
            print(f"node: {k.val}, left: {v[0]}, right: {v[1]}")

        return max_element[0] + max_element[1]