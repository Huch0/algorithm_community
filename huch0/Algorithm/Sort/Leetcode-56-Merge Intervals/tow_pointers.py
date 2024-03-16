class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []

        # Sort the intervals by first element
        intervals = sorted(intervals, key=lambda x: x[0])

        i = 0
        while i < len(intervals):
            interval_start = intervals[i][0]
            interval_end = intervals[i][1]

            # Find the end point of this interval
            j = i
            while j < len(intervals):
                # Not overlapped
                if interval_end < intervals[j][0]:
                    j = j - 1
                    break

                # Overlapped and need to update end of the interval
                if interval_end < intervals[j][1]:
                    interval_end = intervals[j][1]

                j += 1

            # Add to confirmed new interval to the merged_intervals
            merged_intervals.append([interval_start, interval_end])
            i = j + 1

        return merged_intervals
