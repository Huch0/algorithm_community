from collections import defaultdict
from itertools import combinations
import bisect


def solution(info, query):
    answer = []

    info_dict = defaultdict(list)

    for i in info:
        condition = i.split()
        score = int(condition[-1])
        condition = condition[:-1]

        # Calculate all combinations of the condition
        for n in range(5):
            for combi in combinations(range(4), n):
                temp_conditions = condition.copy()

                for idx in combi:
                    temp_conditions[idx] = '-'

                key = ' '.join(temp_conditions)
                info_dict[key].append(score)

    # Sort the score of info_dict
    for key in info_dict:
        info_dict[key].sort()

    # Resolve queries
    for q in query:
        condition = q.split()
        score = int(condition[-1])
        condition = condition[::2]

        key = ' '.join(condition)

        if key in info_dict:
            scores = info_dict[key]
            idx = bisect.bisect_left(scores, score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)

    return answer
