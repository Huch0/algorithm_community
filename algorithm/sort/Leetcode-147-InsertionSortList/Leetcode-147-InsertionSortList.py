# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        cur_node = cur 
        while head :
            while cur_node.next and cur_node.next.val < head.val :
                cur_node = cur_node.next
            temp = head.next
            temp2 = cur_node.next
            cur_node.next = head
            head.next = temp2
            head = temp

            cur_node = cur
        return cur.next