class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_counter = collections.Counter(stones)
        count = 0

        for jewel in jewels:
            count += stone_counter[jewel]
        
        return count
        