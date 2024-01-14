# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        myll = ListNode()
        answer = myll
        p=0
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + p
            p = int(sum/10)
            myll.val = sum%10
            l1, l2 = l1.next, l2.next
            if l1 == None or l2 == None:
                break
            myll.next = ListNode()
            myll = myll.next

        if l1 == None:
            l1 = l2
        if l1 == None:
            if p == 1:
                myll.next = ListNode()
                myll.next.val = 1
            return answer
        
        myll.next = ListNode()
        myll = myll.next
        while True:
            sum = l1.val + p
            p = int(sum/10)
            myll.val = sum%10
            if l1.next == None:
                break
            l1 = l1.next
            myll.next = ListNode()
            myll = myll.next

        if p == 1:
            myll.next = ListNode()
            myll.next.val = 1

        return answer