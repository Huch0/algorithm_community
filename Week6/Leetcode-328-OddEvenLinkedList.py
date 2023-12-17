# using repeat structure

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None :
            return head
        
        odd = head
        even = head.next
        even_first = head.next

        while even and even.next :
           even.next, odd.next  = even.next.next, odd.next.next
           even, odd = even.next, odd.next
        
        odd.next = even_first
        return head
        

"""
first commit 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node and node.next and node.next.next:
            second = node.next
            i = 0
            
            while node and node.next :
                node.next, node = node.next.next, node.next
                
                if node.next is None:
                    node.next = second
                    break
            
                if node.next.next is None and i%2 == 1 :
                    node.next = second
                    break
                
                i += 1

            return head

        else :       
            return head
        
"""