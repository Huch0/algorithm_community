import re


def solution(dartResult):
    answer = 0
    score = [0]

    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    target = re.compile("(\d+)([SDT])([*#]?)")
    rounds = target.findall(dartResult)

    for i in range(len(rounds)):
        if rounds[i][2] == '*':
            score[-1] *= 2
        score.append(int(rounds[i][0]) **
                     bonus[rounds[i][1]] * option[rounds[i][2]])

    return sum(score)
