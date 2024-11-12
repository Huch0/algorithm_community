class Solution:
    def bstToGst(self, root):
        if root:
            self.bstToGst(root.right)
            root.val += self.sum
            self.sum = root.val
            self.bstToGst(root.left)
        return root