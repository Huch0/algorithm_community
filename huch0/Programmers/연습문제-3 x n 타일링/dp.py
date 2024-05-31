def solution(n):
    if n % 2 != 0:
        return 0

    # f(2) = 3, f(4) = 11
    n_4, n_2 = 3, 11

    # f(n) = 4 * f(n - 2) - f(n - 4)
    for i in range(3, (n // 2) + 1):
        n_4, n_2 = n_2, (4 * n_2 - n_4) % 1_000_000_007

    return n_2
