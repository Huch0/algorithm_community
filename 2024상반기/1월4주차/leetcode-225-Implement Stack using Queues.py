class MyStack:

    def __init__(self):
        self.q = collections.deque( )

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int: # 비어있을때 예외처리 안해줌. 최소 1개가 있다고 가정하고 실행
        for i in range(len(self.q)-1):
            n = self.q.popleft()
            self.q.append(n)
        return self.q.popleft()

    def top(self) -> int:
        for i in range(len(self.q)):
            n = self.q.popleft()
            self.q.append(n)
        return n

    def empty(self) -> bool:
        if self.q:
            return 0
        else:
            return 1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()