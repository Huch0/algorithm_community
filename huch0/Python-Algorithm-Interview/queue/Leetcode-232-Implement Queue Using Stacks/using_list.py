class MyQueue:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        # push to top()
        self.stack.append(x)

    def pop(self) -> int:
        tmp = []
        # pop from stack and push to top to tmp
        for i in range(len(self.stack) - 1):
            tmp.append(self.stack.pop())
        
        # this is first element 
        last = self.stack.pop()

        while tmp:
            self.stack.append(tmp.pop())
        
        return last
            

    def peek(self) -> int:
        tmp = []
        while self.stack:
            tmp.append(self.stack.pop())
        
        peek = tmp.pop()
        self.stack.append(peek)

        while tmp:
            self.stack.append(tmp.pop())
        
        return peek


    def empty(self) -> bool:
        return not len(self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()