# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = []

        while queue :
            node = queue.popleft()

            if node :
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else : 
                result.append("#")
        
        print(result)
        return ' '.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == "#" : return None

        data = data.split()
        data_queue = collections.deque(data)

        queue = collections.deque([TreeNode(int(data_queue.popleft()))])
        tree = TreeNode()
        
        i = 0
        while queue and data_queue :
            node = queue.popleft()

            if i == 0 : tree = node

            if not node : continue
            else :
                value = data_queue.popleft()
                if value == "#" : node.left = None
                else : 
                    node.left = TreeNode(int(value))
                    queue.append(node.left)
                
                
                value = data_queue.popleft()
                if value == "#" : node.right = None
                else : 
                    node.right = TreeNode(int(value))
                    queue.append(node.right)
            i += 1
        
        return tree