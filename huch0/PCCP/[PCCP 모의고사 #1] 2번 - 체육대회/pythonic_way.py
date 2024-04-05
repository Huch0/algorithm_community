from itertools import permutations


def solution(ability):
    m = len(ability)
    n = len(ability[0])
    max_sum = 0

    for perm in list(permutations(range(m), n)):
        max_sum = max(max_sum, sum([ability[st][sp]
                      for sp, st in enumerate(perm)]))

    return max_sum
