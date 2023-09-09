# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        odd_root = head
        even_root = head.next

        odd_runner = head
        even_runner = head.next

        while odd_runner and even_runner:
            if even_runner.next == None:
                break
            odd_runner.next = even_runner.next
            odd_runner = odd_runner.next

            even_runner.next = odd_runner.next
            even_runner = even_runner.next

        if odd_runner == None:
            pre_odd = odd_root
            while pre_odd.next == odd_runner:
                pre_odd = pre_odd.next
            odd_runner = pre_odd

        odd_runner.next = even_root

        return odd_root