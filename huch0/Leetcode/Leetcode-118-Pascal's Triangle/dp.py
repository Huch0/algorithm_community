class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [
            [
                1 if j == 1 or j == i else 0 for j in range(1, i + 1)
            ] for i in range(1, numRows + 1)
        ]

        for i in range(2, numRows):
            for j in range(1, i):
                tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]

        return tri
