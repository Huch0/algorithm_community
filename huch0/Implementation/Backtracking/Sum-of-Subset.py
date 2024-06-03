"""_summary_
Problem:
- Given n positive integers (weights) and a postive integer W
- Determine all combinations of the integers that sum to W
Inputs:
- positive integer n
- array of positive integers w indexed from 1 ton n
- positive integer W
Outputs: All possible combinations of the integers that sum to W
"""


def solution(n: int, w: list[int], W: int) -> list[list[bool]]:
    # i : index of the current element
    # weight : sum of the elements included so far
    # total : sum of the remaining elements
    def sum_of_subsets(i: int, weight: int, total: int):
        if promising(i, weight):
            if weight == W:
                solutions.append(include[1:])
            else:
                include[i + 1] = True
                sum_of_subsets(i + 1, weight + w[i + 1], total - w[i + 1])
                include[i + 1] = False
                sum_of_subsets(i + 1, weight, total - w[i + 1])

    def promising(i: int, weight: int) -> bool:
        if i + 1 <= n:
            return (weight + total >= W) and (weight == W or weight + w[i + 1] <= W)
        else:
            return (weight + total >= W) and (weight == W)

    solutions = []
    include = [False] * (n + 1)
    total = sum(w)

    sum_of_subsets(0, 0, total)

    return solutions


if __name__ == "__main__":
    print(solution(4, [0, 3, 4, 5, 6], 13))
