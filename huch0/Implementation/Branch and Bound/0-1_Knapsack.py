from collections import deque


def knapsack(n: int, w: list[int], p: list[int], W: int) -> int:
    def bound(u: tuple[int, int, int]) -> float:
        level, profit, weight = u

        if weight >= W:
            return 0

        result = profit
        j = level + 1
        totweight = weight

        # Grab as many items as possible
        while j <= n and totweight + w[j] <= W:
            totweight += w[j]
            result += p[j]
            j += 1

        # Grab a fraction of the next item
        # "fractional knapsack" upper bound (branch and bound technique)
        k = j
        if k <= n:
            result += (W - totweight) * p[k] / w[k]

        return result
    Q = deque()
    v = (0, 0, 0)  # level, profit, weight

    maxprofit = 0

    Q.append(v)
    while Q:
        level, profit, weight = Q.popleft()
        u = (level + 1, profit + p[level + 1], weight + w[level + 1])

        if u[2] <= W and u[1] > maxprofit:
            maxprofit = u[1]

        # Set u to a child of v
        # 1. u includes the next item
        if bound(u) > maxprofit:
            Q.append(u)

        # 2. u does not include the next item
        # u.profit = v.profit, u.weight = v.weight
        u = (level + 1, profit, weight)
        if bound(u) > maxprofit:
            Q.append(u)

    return maxprofit


if __name__ == "__main__":
    n = 4
    w = [0, 2, 5, 10, 5]
    p = [0, 40, 30, 50, 10]
    W = 16

    print(knapsack(n, w, p, W))
