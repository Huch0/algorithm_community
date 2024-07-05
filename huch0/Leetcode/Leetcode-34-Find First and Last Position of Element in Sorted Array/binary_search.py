class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        l, h = 0, len(nums) - 1
        m = -1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                first, last = m, m
                break
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
        if first == -1:
            return [-1, -1]

        lf, hf = l, m
        while lf <= hf:
            mf = (lf + hf) // 2
            if nums[mf] == target:
                hf = mf - 1
            else:
                lf = mf + 1
        first = lf if nums[lf] == target else hf

        ll, hl = m, h
        while ll <= hl:
            ml = (ll + hl) // 2
            if nums[ml] == target:
                ll = ml + 1
            else:
                hl = ml - 1

        last = hl if nums[hl] == target else ll

        return [first, last]
