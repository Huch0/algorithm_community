class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.queue[self.rear] = value
            return True
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.queue[self.front] = None
            return True
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.queue == [None] * self.size:
            return True

    def isFull(self) -> bool:
        if not(self.isEmpty()) and self.front == (self.rear + 1) % self.size :
            return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()