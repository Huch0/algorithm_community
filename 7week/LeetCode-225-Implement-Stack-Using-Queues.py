from collections import deque

class MyStack:

    def __init__(self):
        self.queue_for_stack = deque()

    
    def push(self, x: int) -> None:
        self.queue_for_stack.append(x)
        for i in range(len(self.queue_for_stack) - 1):
            self.queue_for_stack.append(self.queue_for_stack.popleft())

    def pop(self) -> int:
        if self.empty():
            return
        
        return self.queue_for_stack.popleft()


    def top(self) -> int:
        if self.empty():
            return
        
        return self.queue_for_stack[0]

    def empty(self) -> bool:
        return len(self.queue_for_stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()