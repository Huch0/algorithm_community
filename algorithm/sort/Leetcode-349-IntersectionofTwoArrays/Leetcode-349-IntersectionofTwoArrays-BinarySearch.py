import bisect

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums1.sort()
        for i in nums2 :
            find = bisect.bisect_left(nums1,i)
            if find < len(nums1) and nums1[find] == i :
                result.add(i)
        return result            