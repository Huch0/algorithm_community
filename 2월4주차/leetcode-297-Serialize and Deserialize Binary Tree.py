# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Codec: # 처음 코드. dfs
    def serialize(self, root):
        myarray = []
        def dfs(node):
            if not node:
                myarray.append("null")
            else:
                myarray.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ','.join(map(str, myarray))

    def deserialize(self, data):
        darray = data.split(',')
        darray = [int(element) if element != "null" else None for element in darray]

        def dfs(node):
            if len(darray) == 0:
                return
            
            val = darray.pop(0)
            if val != None:
                node.left = TreeNode(val)
                dfs(node.left)

            val = darray.pop(0)
            if val != None:
                node.right = TreeNode(val)
                dfs(node.right)

        val = darray.pop(0)
        if val != None:
            root = TreeNode(val)
            dfs(root)
            return root

class Codec: # bfs로도 한번 짜봄
    def serialize(self, root):
        dq = collections.deque([root])
        serArray = []
        while dq:
            node = dq.popleft()
            if node != None:
                serArray.append(node.val)
                dq.append(node.left)
                dq.append(node.right)
            else:
                serArray.append("None")
        return ','.join(map(str, serArray))

    def deserialize(self, data):
        deserArray = data.split(',')
        deserArray = [int(element) if element != "None" else None for element in deserArray]
        deserArray = collections.deque(deserArray)
        if deserArray[0] == None:
            return None

        root = TreeNode(deserArray.popleft())
        nodedq = collections.deque([root])
        while nodedq:
            node = nodedq.popleft()

            val = deserArray.popleft()
            if val != None:
                node.left = TreeNode(val)
                nodedq.append(node.left)
            
            val = deserArray.popleft()
            if val != None:
                node.right = TreeNode(val)
                nodedq.append(node.right)

        return root