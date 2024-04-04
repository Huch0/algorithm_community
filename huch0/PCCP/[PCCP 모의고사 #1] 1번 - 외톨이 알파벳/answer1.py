def solution(input_string):
    loner = ''
    encountered = []
    s = input_string + '-'

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            if s[i] in encountered and s[i] not in loner:
                loner += s[i]
            else:
                encountered.append(s[i])

    return ''.join(sorted(loner)) if len(loner) > 0 else 'N'
