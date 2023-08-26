# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        # make reversed_linked list by runner
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        # if ListNode's size is odd, fast == None
        # if ListNode's size is even
        if fast:
            slow = slow.next

        # is_palindrome
        while rev.val == slow.val:
            rev, slow = rev.next, slow.next
        #if ListNode is Palindrome, slow and rev are None
        return not slow