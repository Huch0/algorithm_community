# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, p_left, p_right = ListNode(next=head), head, head
        i = 1

        if not head.next or left == right:
            return head

        while i < right:
            if i < left:
                prev = prev.next
            p_right = p_right.next
            i += 1
        p_left = prev.next
        rev = p_left.next
        #print(head)
        #print(prev.val, p_left.val, rev.val, p_right.val)

        while rev != None:
            prev.next, p_left.next, rev.next = rev, rev.next, prev.next

            if rev == p_right:
                break
            
            rev = p_left.next

            #print(prev.val, p_left.val, rev.val, p_right.val)
            #print(head)

        if left == 1:
            return prev.next
        return head