class Solution(object):
    def swapPairs(self, head):
        node = prev = head
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return prev

# def swapPairs(self, head):
#     if head and head.next:
#         p = head.next
#         head.next = self.swapPairs(p.next)
#         p.next = head
#         return p
#     return head
# reculsive solution