# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 병합 정렬을 이용,
# 1. 분할, Runner 기법을 이용하여 중간을 찾아 분할
# 2. 병합, 분할된 리스트를 정렬된 상태로 병합

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # 1. Runner 기법을 이용하여 중간 위치를 찾음
        # 2. 분할 후 반환
        def merge_sort(start):
            if not start or not start.next:
                return start
            
            slow = fast = start
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            right = slow
            left = start
            while start.next != slow:
                start = start.next
            start.next = None
            
            return merge_list(merge_sort(left), merge_sort(right))

        # 1. 분할된 리스트를 병합
        def merge_list(left, right):

            if not left:
                return right
            if not right:
                return left
            
            head = ListNode()
            
            left_runner, right_runner, runner = left, right, head

            while left_runner and right_runner:
                if left_runner.val < right_runner.val:
                    runner.next = left_runner
                    left_runner = left_runner.next
                else:
                    runner.next = right_runner
                    right_runner = right_runner.next
                runner = runner.next

            if left_runner:
                runner.next = left_runner
            else:
                runner.next = right_runner

            return head.next
        
        return merge_sort(head)