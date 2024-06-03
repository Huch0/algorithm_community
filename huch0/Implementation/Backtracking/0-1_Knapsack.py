"""_summary_
Problem:
Let n items be given, where each item has a weight and a profit.
w[i] > 0 and p[i] > 0 for i = 1, 2, ..., n.
A positive integer W : the maximum weight that can be carried.
Determine a set of items with maximum total profit,
under the constraint that the sum of their weights cannot exceed W.
Inputs:
n : the number of items
W : the maximum weight that can be carried
w : an array indexed from 1 to n, each containing weights of the items
p : an array indexed from 1 to n, each containing profits of the items
w and p are sorted according to the values of p [i] /w [i].
Outputs:
bestset : an array indexed from 1 to n, that contains the optimal set of items.
bestset[i] == True if the ith item is included in the optimal set
bestset[i] == False if the ith item is not included in the optimal set
maxprofit : the maximum profit that can be obtained
"""


def solution(n: int, w: list[int], p: list[int], W: int) -> tuple[int, list[bool]]:
    def knapsack(i: int, profit: int, weight: int) -> int:
        nonlocal maxprofit, numbest, bestset

        if weight <= W and profit > maxprofit:
            maxprofit = profit
            numbest = i
            bestset = include.copy()

        if promising(i, weight, profit):
            include[i + 1] = True
            knapsack(i + 1, profit + p[i + 1], weight + w[i + 1])
            include[i + 1] = False
            knapsack(i + 1, profit, weight)

    def promising(i: int, weight: int, profit: int) -> bool:
        if weight >= W:     # There is no capacity left for children
            return False

        j = i + 1
        bound = profit
        totweight = weight

        # Grab as many items as possible
        while j <= n and totweight + w[j] <= W:
            totweight += w[j]
            bound += p[j]
            j += 1

        # Grab a fraction of the next item
        # "fractional knapsack" upper bound (branch and bound technique)
        k = j
        if k <= n:
            bound += (W - totweight) * p[k] / w[k]

        return bound > maxprofit

    maxprofit = 0
    numbest = 0
    bestset = []
    include = [False] * (n + 1)

    knapsack(0, 0, 0)

    return maxprofit, bestset[1:numbest + 1]


if __name__ == "__main__":
    n = 4
    w = [0, 2, 5, 10, 5]
    p = [0, 40, 30, 50, 10]
    W = 16

    print(solution(n, w, p, W))
