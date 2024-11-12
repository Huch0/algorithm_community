class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        merged = []

        for i in range(len(intervals)):
            currInterval = intervals[i]

            if not merged:
                merged.append(currInterval)
                continue

            if merged[-1][0] <= currInterval[0] <= merged[-1][1]:
                merged[-1] = [min(merged[-1][0], currInterval[0]), max(merged[-1][1], currInterval[1])]
            else:
                merged.append(currInterval)

        return merged