# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        lst = []

        while p:
            lst.append(p.val)
            p = p.next
            
        lst.sort()

        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
    
        return head
        