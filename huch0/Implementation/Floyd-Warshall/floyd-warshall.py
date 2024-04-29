from copy import deepcopy


def print_matrix(matrix: list[list]):
    for row in matrix:
        for e in row:
            if e == float("inf"):
                print("inf ", end="")
            else:
                print("%3d " % e, end="")
        print()


def floyd_warsall(W: list[list]):
    n = len(W) - 1
    D = deepcopy(W)

    print("D(%d) : " % 0)
    print_matrix(D)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

        print("D(%d) : " % k)
        print_matrix(D)


if __name__ == "__main__":
    W = [[0, 0, 0, 0, 0, 0],
         [0, 0, 1, float("inf"), 1, 5],
         [0, 9, 0, 3, 2, float("inf")],
         [0, float("inf"), float("inf"), 0, 4, float("inf")],
         [0, float("inf"), float("inf"), 2, 0, 3],
         [0, 3, float("inf"), float("inf"), float("inf"), 0]]

    floyd_warsall(W)
