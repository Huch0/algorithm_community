
class MyStack:

    def __init__(self):
        # implemented using python's list
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        # pop form front and push to back until last element comes front
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        
        # this is the last element
        return self.queue.pop(0)

    def top(self) -> int:
        top = self.pop()
        self.queue.append(top)
        return top
        

    def empty(self) -> bool:
        return not len(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()