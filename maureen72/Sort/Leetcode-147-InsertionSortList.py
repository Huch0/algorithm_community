# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        def add(node):
            curr = self.ans
            while(curr):
                if(curr.val < node.val):
                    prev = curr
                    curr = curr.next
                else: break
            node.next, prev.next = prev.next, node
            self.ans = ListNode(-5001)
            while(head):
                temp, head = head, head.next
                temp.next = None
                add(temp)
            return self.ans.next