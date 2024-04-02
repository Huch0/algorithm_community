def solution(m, n, board):
    def pang():
        count = 0

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    if mask[i][j] == 0:
                        mask[i][j] = 1
                        count += 1

                    if mask[i + 1][j] == 0:
                        mask[i + 1][j] = 1
                        count += 1

                    if mask[i][j + 1] == 0:
                        mask[i][j + 1] = 1
                        count += 1

                    if mask[i + 1][j + 1] == 0:
                        mask[i + 1][j + 1] = 1
                        count += 1
        return count

    def fall():
        for j in range(n):
            for i in range(m - 1, -1, -1):
                if mask[i][j] != 1:
                    k = i
                    while k < m - 1:
                        if mask[k + 1][j] != 1:
                            break
                        mask[k][j], mask[k + 1][j] = mask[k + 1][j], mask[k][j]
                        board[k][j], board[k + 1][j] = '-', board[k][j]
                        k += 1
                else:
                    board[i][j] = '-'

    mask = [[0] * n for i in range(m)]
    board = [[c for c in s] for s in board]
    count = 0
    pang_cnt = pang()
    while pang_cnt > 0:
        fall()

        count += pang_cnt
        pang_cnt = pang()
    return count


def test():
    m, n = 2, 2
    board = ["CC", "CC"]
    print("test1 : ", solution(m, n, board))

    m, n = 7, 2
    board = ["TT", "CC", "CC", "TT", "CC", "CC", "TT"]
    print("test2 : ", solution(m, n, board))

# test()
