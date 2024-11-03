class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [x * x for x in range(1, int(n**0.5)+1)]
        queue = {n}
        level = 0
        while queue:
            level += 1
            neis = set()
            for i in queue:
                for square in square_nums:
                    if i == square:
                        return level
                    elif i < square:
                        break
                    else:
                        neis.add((i - square))
            queue = neis
