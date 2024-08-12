class Node:
    def __init__(self, item, next):
        self._item = item
        self._next = next

class stack:
    def __init__(self):
        self._last = None
    def push(self, item):
        self._last = Node(item, self._last)
    def pop(self):
        self._last = self._last._next
    def top(self):
        return self._last._item

def main():
    mystack = stack()
    mystack.push(3)
    mystack.push(4)
    mystack.push(5)
    print(mystack.top())
    mystack.pop()
    print(mystack.top())

main()