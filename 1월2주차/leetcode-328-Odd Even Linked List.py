# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = head
        if head == None or head.next == None:
            return head
        even = head.next
        evenstart = even

        while even.next != None and even.next.next != None:
            head.next = even.next
            even.next = head.next.next
            head = head.next
            even = even.next

        if even.next != None:
            head.next = even.next
            head = head.next
            even.next = None
        
        head.next = evenstart
        return answer