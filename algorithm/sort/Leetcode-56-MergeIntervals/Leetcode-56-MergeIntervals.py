class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0],reverse=True)
        level = len(intervals)-1

        result = []

        while level != 0 :
            if  intervals[level][1] >= intervals[level-1][0] :
                intervals[level-1][0] = min(intervals[level-1][0],intervals[level][0])
                intervals[level-1][1] = max(intervals[level-1][1],intervals[level][1])
                intervals.pop()
            else : result.append(intervals.pop())
            level -= 1
        result.append(intervals.pop())
        return result