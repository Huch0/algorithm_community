# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        runner_result = result
        carry = 0

        while l1 or l2 or carry:
            l1_val = 0
            l2_val = 0

            if l1 != None:
                l1_val = l1.val
            if l2 != None:
                l2_val = l2.val

            sum = l1_val + l2_val + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0

            if l1 != None:
                l1 = l1.next

            if l2 != None:
                l2 = l2.next

            runner_result.next = ListNode(sum, None)
            runner_result = runner_result.next

        return result.next