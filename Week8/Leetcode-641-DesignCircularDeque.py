class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.maxlen, self.len = k, 0
        self.head.right = self.tail
        self.tail.left = self.head
    
    def _add(self, node : ListNode, new : ListNode):
        n = node.right
        node.right = new
        new.left, new.right= node, n
        n.left = new
    
    def _del(self,node : ListNode) :
        node.left.right = node.right
        node.right.left = node.left     


    def insertFront(self, value: int) -> bool:
        self.len += 1
        if self.maxlen < self.len :
            self.len -= 1
            return False
        else :
            self._add(self.head, ListNode(value))
            return True

    def insertLast(self, value: int) -> bool:
        self.len += 1
        if self.maxlen < self.len :
            self.len -= 1
            return False
        else :
            self._add(self.tail.left, ListNode(value))
            return True

    def deleteFront(self) -> bool:
        if self.len == 0 : return False
        else :
            self.len -= 1
            self._del(self.head.right)
            return True
        

    def deleteLast(self) -> bool:
        if self.len == 0 : return False
        else :
            self.len -= 1 
            self._del(self.tail.left)
            return True

    def getFront(self) -> int:
        if self.isEmpty() : return -1
        else : return self.head.right.val

    def getRear(self) -> int:
        if self.isEmpty() : return -1
        else : return self.tail.left.val

    def isEmpty(self) -> bool:
        if self.len == 0 : return True
        else : return False

    def isFull(self) -> bool:
        if self.maxlen == self.len : return True
        else : return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()