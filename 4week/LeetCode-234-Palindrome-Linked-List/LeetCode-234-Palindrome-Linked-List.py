# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        #원소의 개수가 홀수일 때
        if fast:
            slow = slow.next
        

        while slow and slow.val == rev.val:
            slow = slow.next
            rev = rev.next
        
        return not rev