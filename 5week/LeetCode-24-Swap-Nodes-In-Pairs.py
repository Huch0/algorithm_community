# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_linked_list(head : ListNode, left : ListNode, right : ListNode) -> ListNode:
    after_right = right.next

    if left == head:
        left.next = after_right
        right.next = left
        head = right
    else:
        pre_left = head
        while pre_left.next != left:
            pre_left = pre_left.next
        pre_left.next = right
        left.next = after_right
        right.next = left

    return head

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        if head.next == None:
            return head
        
        #result = ListNode()
        #original_result = result
        
        odd_runner = head
        even_runner = head.next
        
        while even_runner:
            head = swap_linked_list(head, odd_runner, even_runner)

            odd_runner = odd_runner.next
            if odd_runner == None:
                break
            even_runner = odd_runner.next
        
        return head
            