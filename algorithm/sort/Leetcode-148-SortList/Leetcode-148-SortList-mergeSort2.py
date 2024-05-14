# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2) :
        if l1 and l2 :
            if l1.val > l2.val :
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return head
        
        half, slow, fast = None, head, head
        while fast and fast.next :
            half,slow,fast = slow, slow.next, fast.next.next
        half.next = None

        return(self.mergeTwoLists(self.sortList(head),self.sortList(slow)))