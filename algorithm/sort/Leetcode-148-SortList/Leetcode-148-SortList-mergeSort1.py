# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len_of_linkedlist(self,head) :
        length = 0
        node = head
        while node :
            length += 1
            node = node.next
        return length
    
    def merge(self, head1, head2) :
        result_node = ListNode()
        result = result_node

        while True:

            if head1.val < head2.val :
                result_node.val = head1.val
                head1 = head1.next
                if not head1 : break
            else : 
                result_node.val = head2.val
                head2 = head2.next
                if not head2 : break
            
            result_node.next = ListNode()
            result_node = result_node.next

        if head1 : result_node.next = head1
        elif head2 : result_node.next = head2
        return result

    def merge_sort(self,head) :
        length = self.len_of_linkedlist(head) 
        left = 0
        right = length - 1
        mid = length // 2

        if length <= 1 : return head
        
        mid_linkedlist_node = ListNode()
        mid_linkedlist = mid_linkedlist_node

        level = 0
        while level < mid :
            if level == mid-1 : 
                mid_linkedlist_node.val = head.val
                head=head.next
                level += 1
                continue
                
            mid_linkedlist_node.val = head.val
            mid_linkedlist_node.next = ListNode()
            mid_linkedlist_node = mid_linkedlist_node.next
            head = head.next
            level += 1

        return self.merge(self.merge_sort(mid_linkedlist),self.merge_sort(head))
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head)