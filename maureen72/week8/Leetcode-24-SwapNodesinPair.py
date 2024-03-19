# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
            
        return head
        