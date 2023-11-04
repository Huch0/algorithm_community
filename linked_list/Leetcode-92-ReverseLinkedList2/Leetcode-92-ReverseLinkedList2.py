def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        runnerLeft = runnerRight = head
        while left > 1:
            runnerLeft = runnerLeft.next
            left -= 1
        while right > 1:
            runnerRight = runnerRight.next
            right -= 1
        
        while runnerLeft != runnerRight:
            runnerLeft.val, runnerRight.val = runnerRight.val, runnerLeft.val
            if runnerLeft.next == runnerRight:
                break
            runnerLeft = runnerLeft.next
            runnerRight = runnerRight.prev

        return head
# 'ListNode' object has no attribute 'prev'

# def reverseBetween(self, head, left, right):
#         if not head or left == right:
#             return head
        
#         root = start = ListNode(None)
#         root.next = head

#         for _ in range(left-1):
#             start = start.next

#         end = start.next

#         for _ in range(right-left):
#             tmp, start.next, end.next = start.next, end.next, end.next.next
#             start.next.next = tmp

#         return root.next