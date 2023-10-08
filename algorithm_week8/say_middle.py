import heapq
import sys

n = int(sys.stdin.readline()) # 입력값 받을 때, 이렇게 하면 시간 초과 안 남!

leftHeap = [] # 최대 힙
rightHeap = [] # 최소 힙

for i in range(n):
    num = int(sys.stdin.readline())
    # 핵심. 파이썬의 heapq는 minheap이기 때문에 maxheap을 이용하고 싶으면 음수를 넣어서 최대힙처럼 만들고 pop할 때 다시 음수로 꺼내줘야 한다.
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
        # leftHeap과 rightHeap의 원소 수가 같다면 leftHeap의 최댓값이 중앙값이 된다.
    else:
        heapq.heappush(rightHeap, num)
        # 아니면 우선 rightHeap에 넣고.
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        #rightHeap이 비어있지 않고 rihgtHeap의 가장 작은 원소가 leftHeap의 가장 큰 원소보다 작다면
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)
        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)
        # 서로 위치를 바꿔준다.
        
    print(-leftHeap[0])
    # 결론적으로, leftHeap의 최댓값이(최대힙의 최댓값이) 중앙값이 된다!