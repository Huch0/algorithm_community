# 투포인터 알고리즘 (O(N))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        curlength = 0
        myset = set()
        ptr1, ptr2 = 0, 0

        while ptr2 != len(s):
            if s[ptr2] not in myset: # 이러면 이까지의 길이를 인정해줌
                myset.add(s[ptr2])
                curlength = curlength + 1
                if answer < curlength:
                    answer = curlength
                ptr2 = ptr2 + 1
            else: # ptr1을 다음 칸으로 옮겨줌
                myset.remove(s[ptr1])
                curlength = curlength - 1
                ptr1 = ptr1 + 1
        
        return answer

# 솔루션 : 해시 테이블을 이용해 특정 문자의 index까지 저장해서 진짜 n시간만에 문제 해결
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startIdx = 0
        answer = 0
        used = {} # (문자-index)의 키-값을 저장할 딕셔너리
        for i in range(len(s)):
            if s[i] in used and used[s[i]] >= startIdx:
                startIdx = used[s[i]] + 1
            else:
                curlength = i - startIdx + 1
                if curlength > answer:
                    answer = curlength
            used[s[i]] = i
        return answer