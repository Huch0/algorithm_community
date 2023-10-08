class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. for문 돌면서 슬라이싱을 한다.
        # 2. set으로 만들어서 중복 없는 원소의 개수를 센다
        # 3. 슬라이싱한 크기와 비교하면서 중복이 있는 지 확인한다.

        length = len(s)
        set_length = len(set(s))

        # special case : no duplicate or all duplicate
        if set_length == 1 or set_length == length:
            return set_length
        
        # normal case : min = 2 / max = set_length
        for slice_length in range(set_length, 1, -1):
            for index in range(length - slice_length + 1):
                sliced_str = s[index : index + slice_length]
                if len(sliced_str) == len(set(sliced_str)):
                    return len(sliced_str)
