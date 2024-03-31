# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge_sort(head: ListNode) -> ListNode:
    def divide(head: ListNode) -> ListNode:
        cur = double = head
        prev = None

        while double and double.next:
            prev = cur
            cur = cur.next
            double = double.next.next

        # Divide to two Lists
        if prev:
            prev.next = None

        return cur

    def merge(a: ListNode, b: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next

            tail = tail.next

        tail.next = a or b

        return dummy.next

    # The list is already sorted
    if not head or not head.next:
        return head

    left = head
    right = divide(head)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return merge_sort(head)
