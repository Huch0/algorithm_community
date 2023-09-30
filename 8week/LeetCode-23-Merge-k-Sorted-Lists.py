# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        root_result = result = ListNode(None)
        heap = []

        #비어있지 않은 연결 리스트를 heap에 저장
        #heapq 자료구조를 사용함
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        #heap에서 계속해서 pop을 할 예정
        while heap:
            """
            node에는 (리스트 정렬 기준, 해당 인덱스, 해당 노드)
            
            [
                1->4->5,
                1->3->4,
                2->6
            ]

            와 같은 경우에는 

            [
                (key, 0, 1->3->4)
                (key, 1, 1->4->5)
                (key, 2, 2->6)
            ]
            이라고 가정
            """
            node = heapq.heappop(heap)
            idx = node[1]
            data = node[2]

            #result에 data로 새로 만든 노드 링킹하기
            result.next = data
            result = result.next

            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root_result.next
