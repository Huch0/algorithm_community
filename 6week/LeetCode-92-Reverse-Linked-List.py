# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def get_reverse_linked_list(start: ListNode, end : ListNode) -> ListNode:
        rev = None

        while start != end:
            rev, rev.next, start = start, rev, start.next

        return rev

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        if head == None:
            return head

        after_rev = head
        pre_rev = head

        if left == 1:
            pre_rev = ListNode()
            pre_rev.next = head
        elif left == 2:
            pass
        else:
            while (left - 2):
                pre_rev = pre_rev.next
                left -= 1
        
        while (right):
            after_rev = after_rev.next
            right -= 1

        rev_start = get_reverse_linked_list(pre_rev.next, after_rev)

        pre_rev.next = rev_start

        while rev_start.next is not None:
            rev_start = rev_start.next

        rev_start.next = after_rev

        if left == 1:
            return pre_rev.next
        return head        
