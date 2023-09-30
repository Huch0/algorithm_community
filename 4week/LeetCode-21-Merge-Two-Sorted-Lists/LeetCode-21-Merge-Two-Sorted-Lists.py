# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode()

        result_head = result
        
        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        
        if list1:
            while list1:
                result.next = list1
                list1 = list1.next
                result = result.next
        else:
            while list2:
                result.next = list2
                list2 = list2.next
                result = result.next

        return result_head.next