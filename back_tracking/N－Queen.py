def solve_n_queens(n):
    def backtrack(row, columns, diagonals1, diagonals2):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            diag1 = row - col + n - 1
            diag2 = row + col
            if not (columns[col] or diagonals1[diag1] or diagonals2[diag2]):
                columns[col] = diagonals1[diag1] = diagonals2[diag2] = True
                count += backtrack(row + 1, columns, diagonals1, diagonals2)
                columns[col] = diagonals1[diag1] = diagonals2[diag2] = False
        return count

    columns = [False] * n
    diagonals1 = [False] * (2 * n - 1)
    diagonals2 = [False] * (2 * n - 1)
    return backtrack(0, columns, diagonals1, diagonals2)

def main():
    import sys
    input = sys.stdin.readline
    n = int(input().strip())
    result = solve_n_queens(n)
    print(result)

if __name__ == "__main__":
    main()