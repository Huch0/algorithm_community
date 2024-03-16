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
        result = ""

        # BPS Implementation
        Q = collections.deque()
        Q.append(root)

        while Q:
            cur = Q.popleft()
            if not cur:
                result += "null,"
                continue

            result += str(cur.val) + ","
            Q.append(cur.left)
            Q.append(cur.right)

        # Remove last comma (",")
        result = result[:-1]

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")

        if not nodes or nodes[0] == "null":
            return None

        root = TreeNode(int(nodes[0]))
        Q = collections.deque([root])
        # For tracking current value of nodes
        i = 1

        while Q and i < len(nodes):
            cur = Q.popleft()

            # Add new node to the left
            # And push to the queue for the BFS implementation
            if nodes[i] != "null":
                cur.left = TreeNode(int(nodes[i]))
                Q.append(cur.left)

            i += 1

            if i < len(nodes) and nodes[i] != "null":
                cur.right = TreeNode(int(nodes[i]))
                Q.append(cur.right)

            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
