class Solution(object):
    def reverseList(self, head):
        rev = None
        slow = head
        while slow:
            rev, rev.next, slow = slow, rev, slow.next
        
        return rev

# def reverseList(self, head):
#     def reverse(node, prev=None):
#         if not node:
#             return prev
#         next, node.next = node.next, prev
#         return reverse(next, node)
    
#     return reverse(head)
# recursive를 이용한 풀이