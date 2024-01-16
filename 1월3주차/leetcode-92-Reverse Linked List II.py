# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None:
            return head

        bterm = head
        cur = head.next
        for i in range(left-1):
            p = bterm
            bterm = bterm.next
            cur = cur.next
        if left == 1:
            p = ListNode()
            p.next = head

        for i in range(right-left):
            nterm = cur.next
            cur.next = bterm
            bterm = cur
            cur = nterm

        p.next.next = cur
        p.next = bterm

        if left == 1:
            return p.next
        return head