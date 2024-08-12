# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # 무지성 풀이 (새로운 배열을 만들어도 될 경우)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = []
        for list in lists:
            while list:
                array.append(list.val)
                list = list.next
        array.sort()
        if len(array) == 0:
            return None
        answer = ListNode(array[0])
        node = answer
        for i in range(1, len(array)):
            node.next = ListNode(array[i])
            node = node.next
        return answer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # 새로운 배열 만들기 금지 > 이미 있는 linked list사이의 연결만 바꿔야 한다면 ?
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        MAXVAL = 10000
        answer = ListNode()
        curnode = answer
        while True:
            nextindex = -1
            minval = MAXVAL + 1
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                elif lists[i].val <= minval:
                    minval = lists[i].val
                    nextindex = i
            if nextindex == -1:
                break
            else:
                curnode.next = lists[nextindex]
                curnode = curnode.next
                lists[nextindex] = lists[nextindex].next
        answer = answer.next
        return answer
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # pq를 이용한 해결
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        startnode = ListNode()
        curnode = startnode
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            node = heapq.heappop(heap)
            curnode.next = node[2]
            curnode = curnode.next
            if node[2].next:
                heapq.heappush(heap, (node[2].next.val, node[1], node[2].next))
        
        return startnode.next