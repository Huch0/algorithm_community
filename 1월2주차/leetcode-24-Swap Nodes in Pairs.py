# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 맨앞 맨뒤의 예외처리는 따로 해주고 가운데 2개씩 처리하기

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: #노드가 0개일 경우
            return head
        if head.next == None: #노드가 1개일 경우
            return head
        answer = head.next

        term = head.next.next
        head.next.next = head
        head.next = term

        while True:
            if head.next == None or head.next.next == None:
                break
            term = head.next.next.next # 5저장
            head.next.next.next = head.next # 4.next = 3
            head.next = head.next.next # 1.next = 4
            head.next.next.next = term
            head = head.next.next
        
        return answer