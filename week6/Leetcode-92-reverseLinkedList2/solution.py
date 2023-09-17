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
        for i in range(left-1):
            start = start.next
        
        curr = start.next

        for j in range(right - left):
            next_node = curr.next
            curr.next, start.next, next_node.next = next_node.next, next_node, start.next
        
        return root.next