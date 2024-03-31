class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # t 문자의 카운트를 딕셔너리로 생성
        dict_t = collections.Counter(t)

        required = len(dict_t)  # 필요한 고유 문자 수
        l, r = 0, 0
        formed = 0  # 현재 윈도우에서 필요한 문자가 충족된 수

        window_counts = {}

        ans = float("inf"), None, None  # 윈도우의 길이, 시작 인덱스, 끝 인덱스를 저장

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # 필요한 모든 문자가 현재 윈도우에 포함되어 있으면, l 포인터를 오른쪽으로 이동
            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
