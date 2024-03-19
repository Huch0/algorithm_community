class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val < list2.val:
            merged_list = ListNode(list1.val)
            merged_list.next = self.mergeTwoLists(list1.next, list2)
        else:
            merged_list = ListNode(list2.val)
            merged_list.next = self.mergeTwoLists(list1, list2.next)
        
        return merged_list