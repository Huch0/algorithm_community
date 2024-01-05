# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
            
        