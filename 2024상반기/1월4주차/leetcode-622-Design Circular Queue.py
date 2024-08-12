# 내 풀이 -> pop하더라도 값을 지우고 None으로 만들지 않아도 된다. 대신 꽉 찬 상태를 확인하기 위해 size변수를 따로 관리해야 한다
# 답지 풀이 -> pop하면 값을 지우고 None으로 만들어 준다. 이러면 size변수를 관리할 필요가 없다
# 모듈러 연산을 활용해 포인터 위치가 원형으로 돌아가는걸 구현해주는거 좋은것같다.
class MyCircularQueue:
    def __init__(self, k: int):
        self.circleQueue = [0 for i in range(k)]
        self.capacity = k
        self.size = 0

        self.inIndex = 0 # push했을때 값이 들어갈 곳의 index (0~k-1)
        self.outIndex = 0 # pop했을때 값이 나갈 곳의 index (0~k-1)

    def enQueue(self, value: int) -> bool: # 성공하면 true 반환, 꽉 차있어서 실패하면 false 반환
        if self.isFull():
            return False
        
        self.circleQueue[self.inIndex] = value
        self.inIndex = self.inIndex + 1
        if self.inIndex == self.capacity:
            self.inIndex = 0
        self.size = self.size + 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.outIndex = self.outIndex + 1
        if self.outIndex == self.capacity:
            self.outIndex = 0
        self.size = self.size - 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.circleQueue[self.outIndex]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.circleQueue[self.inIndex - 1]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return 1
        else:
            return 0

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return 1
        else:
            return 0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()