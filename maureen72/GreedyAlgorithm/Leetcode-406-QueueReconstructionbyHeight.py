class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key = lambda person : (-person[0], person[1]))
        res = []
        for h, k in people:
            res.insert(k, [h, k])
        return res