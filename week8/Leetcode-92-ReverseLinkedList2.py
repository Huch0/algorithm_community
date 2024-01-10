# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if head == None:
            return head

        stack = []
        left_node = head
        for i in range(left - 1):
            if left_node == None:
                return head
            left_node = left_node.next

        curr_node = left_node
        for i in range(right - left + 1):
            stack.append(curr_node.val)
            curr_node = curr_node.next
            
        curr_node = left_node
        for i in range(right - left + 1):
            curr_node.val = stack.pop()
            curr_node = curr_node.next

        return head
        