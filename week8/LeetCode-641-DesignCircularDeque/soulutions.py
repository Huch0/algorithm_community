class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None] * k
        self.length = k
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.deque[self.front - 1] is None:
            self.front = (self.front - 1) % self.length
            self.deque[self.front] = value
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.deque[self.rear] is None:
            self.deque[self.rear] = value
            self.rear = (self.rear + 1) % self.length
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.deque[self.front] is not None:
            self.deque[self.front] = None
            self.front = (self.front + 1) % self.length            
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.deque[self.rear - 1] is not None:
            self.deque[self.rear - 1] = None
            self.rear = (self.rear - 1) % self.length
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.deque[self.front] is not None:
            return self.deque[self.front]
        else:
            return -1


    def getRear(self) -> int:
        if self.deque[self.rear - 1] is not None:
            return self.deque[self.rear - 1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.deque[self.front] is None and self.deque[self.rear] is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.front == self.rear and not(self.deque[self.front] is None and self.deque[self.rear] is None):
            return True
        else:
            return False
        


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