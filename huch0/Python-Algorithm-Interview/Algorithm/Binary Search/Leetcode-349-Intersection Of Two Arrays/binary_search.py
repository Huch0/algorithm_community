class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums1, nums2 = sorted(list(set(nums1))), sorted(list(set(nums2)))

        for num in nums1:
            l, h = 0, len(nums2) - 1
            while l <= h:
                m = (l + h) // 2

                if nums2[m] == num:
                    result.append(num)
                    break
                if nums2[m] < num:
                    l = m + 1
                else:
                    h = m - 1

        return result
