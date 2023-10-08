import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))
        
        root = ListNode()
        current = root
        
        while pq:
            val, index, node = heapq.heappop(pq)
            
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(pq, (node.next.val, index, node.next))
        
        return root.next
