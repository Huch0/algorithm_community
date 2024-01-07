class Solution(object):
    def lengthOfLongestSubstring(self, s):
        best = 0
        current = 0
        base = 0
        myDict = {}
        for i in range(len(s)):
            if s[i] not in myDict:
                myDict[s[i]] = i+1
                current += 1
                if current > best:
                    best = current
            else:
                current -= (myDict[s[i]] - base - 1)
                if current <= 0:
                    current = 1
                base = myDict[s[i]] + 1
                myDict[s[i]] = i+1
        
        return best