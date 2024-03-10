class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # 1. 첫 번째 원소를 기준으로 정렬
        intervals.sort(key=lambda x: x[0])
        
        # 2. Overlapping 확인
        def is_overlapping(a, b):
            return a[1] >= b[0]

        def merge_interval(a, b):
            return [a[0], max(a[1], b[1])]
        # 2. 병합
        merged = []

        left = 0

        while left < len(intervals):
            if left < len(intervals)-1 and not is_overlapping(intervals[left], intervals[left+1]):
                merged.append(intervals[left])
                left += 1
            else:
                if left == len(intervals)-1:
                    merged.append(intervals[left])
                    break
                right = left + 1
                current = merge_interval(intervals[left], intervals[right])
                while right < len(intervals)-1 and is_overlapping(current, intervals[right+1]):
                    right += 1
                    current = merge_interval(current, intervals[right])
                merged.append(current)
                left = right+1

        return merged