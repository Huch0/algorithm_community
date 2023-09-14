# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(0)
        prev.next = head

        while(head and head.next):
            swap = head.next
            head.next = swap.next
            swap.next = head

            prev.next = swap

            prev = prev.next.next
            head = head.next

        return root.next