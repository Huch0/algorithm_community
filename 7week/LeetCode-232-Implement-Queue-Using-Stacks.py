class MyQueue:

    def __init__(self):
        self.mid_stack = []
        self.stack_for_queue = []

    def push(self, x: int) -> None:
        self.mid_stack.append(x)
        

    def pop(self) -> int:

        #mid 스택의 값을 다 비우고
        while len(self.mid_stack):
            self.stack_for_queue.append(self.mid_stack.pop())

        #반환할 값을 저장
        result = self.stack_for_queue.pop()

        #큐를 다시 mid 로 보내기
        while len(self.stack_for_queue):
            self.mid_stack.append(self.stack_for_queue.pop())

        return result

    def peek(self) -> int:

        #mid 스택의 값을 다 비우고
        while len(self.mid_stack):
            self.stack_for_queue.append(self.mid_stack.pop())

        #반환할 값을 저장
        result = self.stack_for_queue[-1]

        #큐를 다시 mid 로 보내기
        while len(self.stack_for_queue):
            self.mid_stack.append(self.stack_for_queue.pop())        

        return result

    def empty(self) -> bool:

        return len(self.mid_stack) == 0 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()