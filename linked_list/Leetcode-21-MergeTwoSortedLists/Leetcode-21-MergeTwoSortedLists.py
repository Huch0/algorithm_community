class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result = ListNode(-1)
        cursor = result
        while list1 and list2:
            if list1.val < list2.val:
                cursor.next = list1
                list1 = list1.next
                cursor = cursor.next
            else:
                cursor.next = list2
                list2 = list2.next
                cursor = cursor.next
        
        if list1:
            cursor.next = list1
        if list2:
            cursor.next = list2
        
        return result.next

# def mergeTwoLists(self, l1, l2):
#     if (not l1) or (l2 and l1.val > l2.val):
#         l1, l2 = l2, l1
#     if l1:
#         l1.next = self.mergeTwoLists(l1.next, l2)
#     return l1
#recursive 풀이