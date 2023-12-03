# using runner

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        rev = None

        while fast and fast.next :
            fast = fast.next.next

            rev, rev.next, slow = slow, rev, slow.next
        
        if fast : slow = slow.next

        while slow :
            if slow.val != rev.val : return False
            slow, rev = slow.next, rev.next
        
        return True

"""
# using list

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        List = []

        node = head

        while node is not None :
            List.append(node.val)
            node = node.next
        
        if List == List[::-1] : return True
        else : False

"""