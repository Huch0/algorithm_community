"""_summary_
Problem: Position n queens on a chessboard so that no two are in the same row, column, or diagonal.
Inputs: positive integer n
Outputs:
- all possible ways n queens can be placed on an n x n chessboard so that no two queens threaten each other.
- Each output consisits of an array of integers col indexed from 1 to n, where col[i] is the column where the queen in the ith row is placed.
"""


def n_queens(n: int) -> list[list[int]]:
    def queens(i: int):
        print(i, col[1:], promising(i))
        if promising(i):
            if i == n:
                solutions.append([col[k] for k in range(1, n + 1)])
            else:
                for j in range(1, n + 1):
                    col[i + 1] = j
                    queens(i + 1)

    def promising(i: int) -> bool:
        k = 1
        switch = True

        while k < i and switch:
            if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
                switch = False
            k += 1

        return switch

    solutions = []
    col = [0] * (n + 1)

    queens(0)

    return solutions


if __name__ == "__main__":
    print(n_queens(4))
    # print(n_queens(8))
