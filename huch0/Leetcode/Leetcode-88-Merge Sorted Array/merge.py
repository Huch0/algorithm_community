class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = []
        nums1_copy = nums1[:m]
        i = 0
        j = 0
        for _ in range(m + n):
            if i >= m:
                merged.extend(nums2[j:])
                break
            elif j >= n:
                merged.extend(nums1_copy[i:])
                break

            if nums1_copy[i] < nums2[j]:
                merged.append(nums1_copy[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        nums1[:] = merged
