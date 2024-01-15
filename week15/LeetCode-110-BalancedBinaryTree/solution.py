주어진 이진 트리의 서브 트리간의 높이 차이가 1인지 판단하는 코드
def isBalanced(self, root: TreeNode) -> bool:
    left, right = 0, 0
    level = 0
    def levelCheck(prev, root):    
        nonlocal level
        
        if not root:    
            return
        level += 1
        
        levelCheck(root, root.left)
        levelCheck(root, root.right)
        return level

    left = levelCheck(None, root.left)
    right = levelCheck(None, root.right)