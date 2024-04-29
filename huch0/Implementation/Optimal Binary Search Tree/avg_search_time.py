"""
void optsearchtree(int n, const float p[], float &minavg, int R[][MAXN+1]) {
    index i, j, k, diagonal;
    float A[1..n + 1][0..n];

    for (i = 1; i <= n; i++) {
        A[i][i - 1] = 0;
        A[i][i] = p[i];
        R[i][i] = i;
        R[i][i - 1] = 0;
    }

    A[n + 1][n] = 0;
    R[n + 1][n] = 0;

    for (diagonal = 1; diagonal <= n - 1; diagonal++) {
        for (i = 1; i <= n - diagonal; i++) {
            j = i + diagonal;
            A[i][j] = minimum_{i<=k<=j}(A[i][k - 1] + A[k + 1][j]) + sum(p[i..j]);
            R[i][j] = k;
        }
    }

    minavg = A[1][n];
"""

# A[1][n] = minimum_{1<=k<=n}(A[1][k - 1] + A[k + 1][n]) + sum(p[1..n])
# Range of A: [1..n+1][0..n]
# Meaning of R[i][j]: The root of the optimal subtree for keys ki, ki+1, ..., kj
"""
    n : The number of keys
    p : The probabilities of accessing the keys
    minavg : The minimum average search time
    R : The root of the optimal subtree
"""


def optsearchtree(n: int, p: list[float]) -> float:
    A = [[0] * (n + 1) for _ in range(n + 2)]  # index 0 is not used
    R = [[0] * (n + 1) for _ in range(n + 2)]  # index 0 is not used

    # base cases
    # A[i][i] = p[i]
    # A[i][i - 1] = 0
    for i in range(1, n+1):
        A[i][i] = p[i]
        A[i][i-1] = 0

        R[i][i] = i
        R[i][i-1] = 0

    A[n+1][n] = 0
    R[n+1][n] = 0

    # For each diagonal : representing the subtree size
    for diagonal in range(1, n):
        print(f"diagonal: {diagonal}")
        # For each starting index i
        for i in range(1, n-diagonal+1):
            # Calculate the ending index j
            j = i + diagonal
            # Minimum average search time for the subtree 'rooted at i' and spanning i to j
            A[i][j] = min(A[i][k-1] + A[k+1][j]
                          for k in range(i, j+1)) + sum(p[i:j+1])
            # Optimal root index for this subtree
            R[i][j] = min(range(i, j+1), key=lambda k: A[i][k-1] + A[k+1][j])
            print(f"i: {i}, j: {j}, A[i][j]: {A[i][j]}")

        print("A:")
        for row in A:
            print(" ".join(f"%.2f" % elem for elem in row))
        print()

    minavg = A[1][n]
    print("Roots of the optimal subtree:")
    for row in R:
        print(row)

    print("A:")
    for row in A:
        print(" ".join(f"%.3f" % elem for elem in row))

    return minavg


if __name__ == "__main__":
    n = 4
    p = [0, 3/8, 3/8, 1/8, 1/8]
    minavg = optsearchtree(n, p)
    print(minavg)
