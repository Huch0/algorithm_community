class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head :
            rev, rev.next, head = head, rev, head.next
        return rev