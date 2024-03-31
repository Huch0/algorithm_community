# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handle special cases ([], [1])
        if not head or not head.next:
            return head

        # track odd nodes
        odd = head 
        # track even nodes
        even = odd.next
        # track last node
        last = head
        # to decide the number of iteration
        count, length = 1, 1

        while last.next:
            last = last.next
            length += 1

        while even and even.next and count <= length // 2:
            odd.next = even.next

            last.next = even

            odd, even, last = odd.next, even.next.next, last.next
            last.next = None
            count += 1

        return head
        