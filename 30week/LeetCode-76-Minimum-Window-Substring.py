from collections import deque, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = deque()

        results = []
        window_dict = Counter(t)

        for v in s:
            window.append(v)

            if window_dict[v] is not None:
                window_dict[v] -= 1
                if window and not any([window_dict[char] > 0 for char in window_dict.keys()]):
                    while window and not (window_dict[window[0]] == 0):
                        if window_dict[window[0]]:
                            window_dict[window[0]] += 1
                        window.popleft()
                    
                    if not any([window_dict[char] > 0 for char in window_dict.keys()]):
                        results.append("".join(window))
        
        if results:
            return min(results, key=len)
        else:
            return ""
        
    #def minWindow(s: str, t: str) -> str:
    #if not t or not s:
    #     return ""

    # # t의 문자들에 대한 카운터 생성
    # dict_t = Counter(t)

    # required = len(dict_t)

    # # 윈도우 포인터와 필요한 문자의 개수 초기화
    # l, r = 0, 0
    # formed = 0
    # window_counts = {}

    # # 결과를 저장할 변수 (윈도우 길이, 시작 인덱스, 끝 인덱스)
    # ans = float("inf"), None, None

    # while r < len(s):
    #     character = s[r]
    #     window_counts[character] = window_counts.get(character, 0) + 1

    #     if character in dict_t and window_counts[character] == dict_t[character]:
    #         formed += 1

    #     # 모든 필요한 문자가 포함될 때까지 l을 이동시키며 윈도우 크기 조정
    #     while l <= r and formed == required:
    #         character = s[l]

    #         if r - l + 1 < ans[0]:
    #             ans = (r - l + 1, l, r)

    #         window_counts[character] -= 1
    #         if character in dict_t and window_counts[character] < dict_t[character]:
    #             formed -= 1

    #         l += 1

    #     r += 1

    # return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
