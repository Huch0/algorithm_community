# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        root = start = ListNode(0)
        start.next = head
        for i in range(left):
            start_root = start
            start = start.next
        
        prev = start_root 
        end = start

        for j in range(right - left):
            print(head)
            swap = end
            end = end.next
            swap.next = prev
            prev = swap

        start.next = end.next
        end.next = prev
        start_root.next = end
        
        return root.next