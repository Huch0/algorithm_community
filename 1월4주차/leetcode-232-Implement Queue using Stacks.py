# 처음 풀이 - push할때마다 매번 다 꺼내줘야해서 오래걸림
class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        termStack = []
        while self.stack:
            termStack.append(self.stack.pop())
        self.stack.append(x)
        while termStack:
            self.stack.append(termStack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if self.stack:
            return 0
        else:
            return 1
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
        
# 개선된 풀이 - 전체적으로 O(1)에 해결 가능
class MyQueue:

    def __init__(self):
        self.inputstack = []
        self.outputstack = []

    def push(self, x: int) -> None:
        self.inputstack.append(x)

    def pop(self) -> int:
        if not self.outputstack:    
            while self.inputstack:
                self.outputstack.append(self.inputstack.pop())
        return self.outputstack.pop()

    def peek(self) -> int:
        if not self.outputstack:    
            while self.inputstack:
                self.outputstack.append(self.inputstack.pop())
        return self.outputstack[-1]

    def empty(self) -> bool:
        if self.inputstack or self.outputstack:
            return 0
        else:
            return 1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()