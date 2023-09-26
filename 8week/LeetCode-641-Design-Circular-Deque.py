class ListNode:
    def __init__(self, prev = None, val = None, next=None):
        self.prev = prev
        self.val = val
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.count_element = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.head = ListNode(val = value)

            self.count_element += 1

            self.tail = self.head
            return True
        
        elif self.isFull():
            return False
        
        else:
            #새로운 노드 생성 후 head와 링킹
            new_Node = ListNode(val = value, next=self.head)
            self.head.prev = new_Node

            #원소 개수 늘리기
            self.count_element += 1
            
            #헤드 변경
            self.head = new_Node

            #만약 방금 원소의 개수를 늘려서 원형 데큐가 가득찼다면 tail과도 링킹
            if self.isFull():
                self.tail.next = new_Node
                self.head.prev = self.tail

            return True

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.tail = ListNode(val = value)
            
            self.count_element += 1

            self.head = self.tail
            return True
        
        elif self.isFull():
            return False
        
        else:
            #새로운 노드 생성 후 tail과 링킹
            new_Node = ListNode(val = value, prev=self.tail)
            self.tail.next = new_Node

            #원소 개수 늘리기
            self.count_element += 1
            
            #테일 변경
            self.tail = new_Node

            #만약 방금 원소의 개수를 늘려서 원형 데큐가 가득찼다면 tail과도 링킹
            if self.isFull():
                self.tail.next = self.head
                self.head.prev = self.tail

            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        original_head = self.head
        self.head = self.head.next

        del original_head

        self.count_element -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        original_tail = self.tail
        self.tail = self.tail.prev

        del original_tail

        self.count_element -= 1

        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.count_element == 0

    def isFull(self) -> bool:
        return self.count_element == self.max_size        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()