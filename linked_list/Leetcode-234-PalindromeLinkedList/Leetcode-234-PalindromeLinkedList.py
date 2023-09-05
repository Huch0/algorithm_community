class Solution(object):
    def isPalindrome(self, head):
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
#runner 기법을 이용한 풀이

# def isPalindrome(self, head):
#     q: Deque = collections.deque()

#     if not head:
#         return True

#     node = head
#     while node is not None:
#         q.append(node.val)
#         node = node.next
    
#     while len(q) > 1:
#         if q.popleft() != q.pop():
#             return False

#     return True
# deque를 이용한 풀이