class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        alpha = {}
        
        for i in stones:
            if i not in alpha:
                alpha[i] = 1
            else:
                alpha[i] += 1
        
        cnt = 0
        for j in jewels:
            if j in alpha:
                cnt += alpha[j]
        
        return cnt