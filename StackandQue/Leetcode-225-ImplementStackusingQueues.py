class MyStack(object):

    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for i in range(0,len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]
        

    def empty(self):
        if len(self.q) == 0:
            return True
        else:
            return False

