class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        while i < m and j < n and nums1[i] is not None and nums2[j] is not None:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i == m:
            nums += nums2[j:]
        elif j == n:
            nums += nums1[i:]

        median = 0
        l = len(nums)
        if l % 2 == 0:
            median = (nums[l // 2 - 1] + nums[l // 2]) / 2
        else:
            median = nums[l // 2]

        return median
