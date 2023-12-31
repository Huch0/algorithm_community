class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        myDict = {}
        total = 0

        for char in stones:
            if char in myDict:
                myDict[char] += 1
            else:
                myDict[char] = 1

        for jewel in jewels:
            if jewel in myDict:
                total += myDict[jewel]

        return total