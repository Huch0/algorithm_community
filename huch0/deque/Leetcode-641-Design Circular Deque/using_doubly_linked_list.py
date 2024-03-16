class MyCircularDeque:
    # Node for Doubly Linked List
    class Node:
        def __init__(self, val: int):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        # Sentinel Nodes for Doubly Linked List
        self.header = self.Node(None)
        self.trailer = self.Node(None)
        # header <-> trailer
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        front = self.header.next
        new_front = self.Node(value)

        self.header.next = new_front
        new_front.prev = self.header

        new_front.next = front
        front.prev = new_front

        self.size += 1

        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        last = self.trailer.prev
        new_last = self.Node(value)

        self.trailer.prev = new_last
        new_last.next = self.trailer

        new_last.prev = last
        last.next = new_last

        self.size += 1

        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return 0
        
        front = self.header.next
        new_front = front.next

        self.header.next = new_front
        new_front.prev = self.header

        self.size -= 1

        return 1
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return 0
        last = self.trailer.prev
        new_last = last.prev

        self.trailer.prev = new_last
        new_last.next = self.trailer

        self.size -=1

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.header.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.trailer.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.capacity


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