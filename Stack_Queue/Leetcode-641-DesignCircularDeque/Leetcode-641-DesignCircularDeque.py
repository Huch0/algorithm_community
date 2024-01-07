class MyCircularDeque(object):

    def __init__(self, k):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        

    def _add(self, node, new):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    
    def _del(self, node):
        n = node.right.right
        node.right = n
        n.left = node

        
    def insertFront(self, value):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
        

    def insertLast(self, value):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
        

    def deleteFront(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True


    def deleteLast(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
        

    def getFront(self):
        return self.head.right.val if self.len else -1
        

    def getRear(self):
        return self.tail.left.val if self.len else -1
        

    def isEmpty(self):
        return self.len == 0
        

    def isFull(self):
        return self.len == self.k
