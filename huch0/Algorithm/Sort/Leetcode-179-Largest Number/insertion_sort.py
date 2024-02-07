class Solution:
    @staticmethod
    def compare(a: int, b: int) -> bool:
        return str(a) + str(b) < str(b) + str(a)

    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.compare(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        result = ''.join(map(str, nums))

        if result[0] == '0':
            return '0'

        return result
