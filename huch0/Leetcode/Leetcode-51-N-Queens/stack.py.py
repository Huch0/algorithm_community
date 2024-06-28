class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers = []

        mid = n // 2
        if n % 2 == 1:
            mid += 1

        for i in range(mid):
            stack = []
            stack.append([i])

            while stack:
                cols = stack.pop()

                if len(cols) == n:
                    answers.append(cols)
                    continue

                for j in range(n - 1, -1, -1):
                    if self.is_promising(cols, len(cols), j):
                        stack.append(cols + [j])

        # Convert cols into str
        answers = [['.' * i + 'Q' + '.' * (n - i - 1) for i in answer] for answer in answers]
        # Mirror except for the middle ones
        answers += [[s[::-1] for s in answer] for answer in list(reversed((answers))) if answer[0][n//2] != 'Q']

        return answers

    @staticmethod
    def is_promising(cols, i, j):
        for k in range(i):
            if cols[k] == j or abs(cols[k] - j) == abs(k - i):
                return False
        return True
