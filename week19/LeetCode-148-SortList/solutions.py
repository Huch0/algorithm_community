# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elements = []
        tmp = head
        while tmp:
            elements.append(tmp.val)
            tmp = tmp.next

        elements.sort()

        tmp = head
        for i in range(len(elements)):
            tmp.val = elements[i]
            tmp = tmp.next
        return head

