class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = deque()
        for person in people:
            queue.insert(person[1], person)

        return list(queue)