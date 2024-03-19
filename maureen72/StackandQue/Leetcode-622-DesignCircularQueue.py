class MyCircularQueue(object):

    def __init__(self, k): 
        self.queue = [None] * k
        self.capacity = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value):
        if self.isFull():
            return False


        self.queue[self.p2] = value
        self.p2 = (self.p2 + 1) % self.capacity

        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.queue[self.p1] = None
        self.p1 = (self.p1 + 1) % self.capacity

        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.p1]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.p2 - 1]
        

    def isEmpty(self):
        return self.p1 == self.p2 and not self.queue[self.p1]
        
    def isFull(self):
        return self.p1 == self.p2 and self.queue[self.p2]


