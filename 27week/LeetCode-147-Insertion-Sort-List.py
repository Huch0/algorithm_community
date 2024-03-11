# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Test Case : 4 2 1 3
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        prev_runner = head
        runner = head.next
        next_runner = runner.next

        def find_bigger_element_in_left(head, runner):
            while head != runner:
                if head.val > runner.val:
                    break
                head = head.next
            # find X
            return head
        
        def find_prev_node(head, target):
            if head == target:
                return None
            while head.next != target:
                head = head.next
            return head

        while runner:
            node = find_bigger_element_in_left(head, runner)
            
            # 삽입이 일어난 경우
            if node != runner:
                prev_runner = find_prev_node(head, runner)
                prev_node = find_prev_node(head, node)
                if prev_node:
                    prev_node.next = runner
                else:
                    head = runner
                runner.next = node

                prev_runner.next = next_runner
            else:
                prev_runner = runner

            runner = next_runner
            if not runner:
                break
            next_runner = runner.next

        return head