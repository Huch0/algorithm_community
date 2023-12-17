# Reorder using a stack when peek() (with two stacks)

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
 
    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:      
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output :
            while self.input :
                self.output.append(self.input.pop())
        return self.output[-1] 

    def empty(self) -> bool:
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
Reorder using a stack when push() (with two stacks)

class MyQueue:

    def __init__(self):
        self.stack = []
        self.spare = []
    def push(self, x: int) -> None:
        if len(self.stack) == 0 : 
            self.stack.append(x)
            print(self.stack)
        
        else :
            for i in range(len(self.stack)) :
                self.spare.append(self.stack.pop())
            self.stack.append(x)
            for i in range(len(self.spare)) :
                self.stack.append(self.spare.pop())
            print(self.stack)
            

    def pop(self) -> int:
        return self.stack.pop()
        

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not len(self.stack)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
"""