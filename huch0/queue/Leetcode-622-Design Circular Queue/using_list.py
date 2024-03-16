class MyCircularQueue:
    def __init__(self, k: int):
        # Initiate container 
        self.queue = [None] * k
        # to store capacity of container
        self.capacity = k
        # to track front index 
        self.front = 0
        # to track rear index
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # queue.Push(value)
        self.queue[self.rear] = value
        # Move rear pointer
        self.rear = (self.rear + 1) % self.capacity

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        # queue.pop(0)
        self.queue[self.front] = None
        # Move front pointer
        self.front = (self.front + 1) % self.capacity

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear - 1]
        

    def isEmpty(self) -> bool:
        # if there is a value in Queue[front], it is not empty
        return self.front == self.rear and not self.queue[self.front]
        
    def isFull(self) -> bool:
        # if there is no value in Queue[rear], it is not full
        return self.front == self.rear and self.queue[self.rear]
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()