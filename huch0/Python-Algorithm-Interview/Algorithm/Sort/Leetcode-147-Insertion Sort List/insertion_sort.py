# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = sorted_head = ListNode()

        while head:
            # Find the proper position for current node
            while pos.next and head.val > pos.next.val:
                pos = pos.next

            # Insert node to the proper position
            pos.next, head.next, head = head, pos.next, head.next

            # Move pos to the sorted_head if necessary
            if head and head.val < pos.val:
                pos = sorted_head

        return sorted_head.next
