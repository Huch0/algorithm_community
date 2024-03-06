class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # to find shorter list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # change nums1(shorter one) to set 
        num1_set = set(nums1)
        
        ans = []

        # find intersection
        for num in nums2:
            if num in num1_set and num not in ans:
                ans.append(num)

        return ans