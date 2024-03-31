# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tracer = head
        rev = None

        while tracer != None:
            # it worked
            rev, tracer.next, tracer = tracer, rev, tracer.next
            # didn't work
            #rev, tracer, tracer.next = tracer, tracer.next, rev

        return rev
        