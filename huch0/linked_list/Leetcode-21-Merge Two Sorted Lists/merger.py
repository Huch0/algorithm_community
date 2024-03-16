# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        merger = merged

        while list1 or list2:
            if not list1:
                merger.next, list2 = list2, list2.next
                merger = merger.next
                continue
            if not list2:
                merger.next, list1 = list1, list1.next
                merger = merger.next
                continue
                
            if list1.val <= list2.val:
                merger.next, list1 = list1, list1.next
                merger = merger.next
            else:
                merger.next, list2 = list2, list2.next
                merger = merger.next
        
        return merged.next