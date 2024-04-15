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
        result = ['#']

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
        if data == "# #" : return None

        data_list = data.split()

        root = TreeNode(data_list[1])
        queue = collections.deque([root])

        index = 2

        while queue :
            node = queue.popleft()

            if data_list[index] == '#' : 
                pass
            else : 
                node.left = TreeNode(data_list[index])
                queue.append(node.left)
            index += 1

            if data_list[index] == '#' : 
                pass
            else : 
                node.right = TreeNode(data_list[index])
                queue.append(node.right)
            index += 1

        return root