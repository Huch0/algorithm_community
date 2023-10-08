class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dicts = {}
        for jewel in jewels:
            dicts[jewel] = 0

        for stone in stones:
            if stone in jewels:
                dicts[stone] += 1
        
        count = 0

        for key in dicts:
            count += dicts[key]

        return count