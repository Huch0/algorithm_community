# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        # Store the roots of the each lists in to heap 
        for i in range(len(lists)):
            if lists[i]:
                # lists[i].val : Value for sorting.
                # i : index for prevent duplicate in heap
                # lists[i] : Node 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
            
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next

            # Store next node to heap
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
            
        
        return root.next
        