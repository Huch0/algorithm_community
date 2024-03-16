class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        q = []
        for p in people:
            heapq.heappush(heap, [-p[0], p[1]])

        while heap:
            person = heapq.heappop(heap)
            q.insert(person[1], [-person[0], person[1]])

        return q
