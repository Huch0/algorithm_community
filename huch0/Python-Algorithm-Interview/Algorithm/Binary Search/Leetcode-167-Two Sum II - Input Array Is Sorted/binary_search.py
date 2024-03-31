class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i, n1 in enumerate(numbers):
            diff = target - n1
            l, h = i + 1, n - 1

            # Search the diff in the array
            while l <= h:
                m = (l + h) // 2

                n2 = numbers[m]
                if n2 == diff:
                    return [i + 1, m + 1]
                if n2 < diff:
                    l = m + 1
                else:
                    h = m - 1
