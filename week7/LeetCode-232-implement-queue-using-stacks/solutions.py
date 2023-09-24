class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        n = len(self.input) - 1
        for i in range(n):
            self.output.append(self.input.pop())
        res = self.input.pop()
        for i in range(n):
            self.input.append(self.output.pop())
        return res

    def peek(self) -> int:
        n = len(self.input) - 1
        for i in range(n):
            self.output.append(self.input.pop())
        res = self.input[0]
        for i in range(n):
            self.input.append(self.output.pop())
        return res

    def empty(self) -> bool:
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()