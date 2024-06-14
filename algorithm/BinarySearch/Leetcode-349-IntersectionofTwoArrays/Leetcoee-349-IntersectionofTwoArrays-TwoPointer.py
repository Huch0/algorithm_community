class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        
        nums1.sort()
        nums2.sort()

        nums1_pointer = 0
        nums2_pointer = 0

        while nums1_pointer < len(nums1) and nums2_pointer < len(nums2) :
            if nums1[nums1_pointer] < nums2[nums2_pointer] :
                nums1_pointer += 1
            elif nums1[nums1_pointer] > nums2[nums2_pointer] :
                nums2_pointer += 1
            else : 
                result.add(nums1[nums1_pointer])
                nums1_pointer += 1
                nums2_pointer += 1
        
        return result