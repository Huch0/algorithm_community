# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            # before : rev / slow -> slow.next
            # after : rev(before) <- rev / slow 
            rev, rev.next, slow = slow, rev, slow.next
        
        # if the lenth of list is odd 
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        
        return not rev