import functools

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        str_nums = [str(num) for num in nums]

        def compare(x, y):
            if len(x) == len(y):
                return int(x) - int(y)
            elif len(x) > len(y):
                if x[:len(y)] == y:
                    return compare(x + y, y + x)
                else:
                    return int(x[:len(y)]) - int(y)
            else: 
                return -1 * compare(y, x)

        str_nums.sort(key=functools.cmp_to_key(compare), reverse=True)

        return ''.join(str_nums).lstrip('0') or '0'
