# 요소의 유무만 판단하면 되므로 set으로 푸는게 좋다
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jlist = list(jewels)
        answer = 0
        for c in stones:
            if c in jlist:
                answer = answer + 1
        return answer

#defaultdict 연습해보기
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        mydict = collections.defaultdict(int)
        for c in stones:
            mydict[c] = mydict[c]+1
        
        answer = 0
        for c in jewels:
            answer = answer + mydict[c]
        return answer