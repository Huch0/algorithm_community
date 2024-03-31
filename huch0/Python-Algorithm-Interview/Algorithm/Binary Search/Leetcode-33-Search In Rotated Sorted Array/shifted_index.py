class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find minimum value
        n = len(nums)
        l, h, min_index = 0, n - 1, 0

        while l <= h:
            m = (l + h) // 2

            if h - l == 1:
                if nums[m] < nums[h]:
                    min_index = m
                else:
                    min_index = h
                break

            if nums[m] < nums[(m - 1) % n] and nums[m] < nums[(m + 1) % n]:
                # Minimum value is found
                min_index = m
                break
            else:
                if nums[h] < nums[l] < nums[m]:  # Find righthand side
                    l = m + 1
                else:  # Find lefthand side
                    h = m - 1

        # Find target with shifted index
        l, h = 0, n - 1
        while l <= h:
            m = (l + h) // 2
            shifted_m = (m + min_index) % n
            if nums[shifted_m] == target:
                return shifted_m

            if nums[shifted_m] < target:
                l = m + 1
            else:
                h = m - 1

        return -1
