# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return head 

        List = []
        p = head
        while p :
            List.append(p.val)
            p = p.next
        
        List.sort()

        p = head
        for i in range(len(List)) :
            p.val = List[i]
            p = p.next
        return head
        