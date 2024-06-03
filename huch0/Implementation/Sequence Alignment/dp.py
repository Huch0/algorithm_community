def sequence_alignment(x: list, y: list, m: int = 5, s: int = -3, d: int = -4):
    m = len(x)
    n = len(y)
    F = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    Ptr = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialization
    F[0][0] = 0
    for j in range(1, n + 1):
        F[0][j] = d * j
        Ptr[0][j] = '←'
    for i in range(1, m + 1):
        F[i][0] = d * i
        Ptr[i][0] = '↑'

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            F[i][j] = max(
                F[i - 1][j - 1] + (m if x[i - 1] == y[j - 1] else s),  # case1 match/mismatch
                F[i - 1][j] + d,  # case2
                F[i][j - 1] + d,  # case3
            )
            if F[i][j] == F[i - 1][j - 1] + (m if x[i - 1] == y[j - 1] else s):
                # case 1
                Ptr[i][j] = '↖'
            elif F[i][j] == F[i - 1][j] + d:
                # case 2
                Ptr[i][j] = '↑'
            else:
                # case 3
                Ptr[i][j] = '←'

    # score(m, n)
    print_F(F, x, y)
    print_Ptr(Ptr)

    # Traceback
    i, j = m, n
    x_align = []
    y_align = []
    while i > 0 or j > 0:
        if Ptr[i][j] == '↖':
            x_align.append(x[i - 1])
            y_align.append(y[j - 1])
            i -= 1
            j -= 1
        elif Ptr[i][j] == '↑':
            x_align.append(x[i - 1])
            y_align.append('-')
            i -= 1
        else:
            x_align.append('-')
            y_align.append(y[j - 1])
            j -= 1

    x_align.reverse()
    y_align.reverse()
    print("".join(x_align))
    print("".join(y_align))


def print_F(F, x, y):
    print("-  - ", end=" ")
    for elem in y:
        print("%3s" % elem, end=" ")
    print()
    for i, row in enumerate(F):
        if i == 0:
            print("-", end=" ")
        else:
            print("%s" % x[i - 1], end=" ")

        for elem in row:
            print("%3d" % elem, end=" ")
        print()


def print_Ptr(Ptr):
    for row in Ptr:
        for elem in row:
            print(elem, end=" ")
        print()


if __name__ == "__main__":
    x_seq = "CATAC"
    y_seq = "ATCGAC"

    sequence_alignment(x_seq, y_seq)
