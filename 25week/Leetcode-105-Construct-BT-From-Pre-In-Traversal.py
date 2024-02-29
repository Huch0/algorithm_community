# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.val}'

#step 1 : preorder의 순서를 활용하여 inorder list의 높이를 저장
#step 2 : 높이를 바탕으로 자식을 연결
#step 3 : root 반환
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        node_height = {}
        for i in range(len(preorder)):
            node_height[preorder[i]] = len(preorder) - i - 1

        inorder_to_Treenode = [TreeNode(val) for val in inorder]
        
        def find_node(val):
            for node in inorder_to_Treenode:
                if node.val == val:
                    return node
                
        def list_cutting(list, height):
            factor = 0
            for val in list:
                if node_height[val] > height:
                    break
                factor += 1
            if factor != 0:
                list = list[:factor]
                return list
            else:
                return None

        def make_tree(node_val):
            current_node = find_node(node_val)
            current_x = inorder.index(node_val)
            left_child = right_child = None
            left = inorder[:current_x][::-1]
            right = inorder[current_x + 1:]
            # 왼쪽에 연결할 수 있는 노드를 찾는다.
            left_cutted = list_cutting(left, node_height[node_val])
            if left_cutted:
                left_child = max(left_cutted, key = lambda x : node_height[x])   
            # 오른쪽에 연결할 수 있는 노드를 찾는다.
            right_cutted = list_cutting(right, node_height[node_val])
            if right_cutted:
                right_child = max(right_cutted, key = lambda x : node_height[x])

            #print(current_node, left_cutted, right_cutted)
            if left_child:
                current_node.left = find_node(left_child)
            if right_child:
                current_node.right = find_node(right_child)

        for val in preorder:
            make_tree(val)
            #print()

        return find_node(preorder[0])