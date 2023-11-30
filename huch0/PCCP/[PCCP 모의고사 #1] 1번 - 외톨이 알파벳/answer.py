def solution(input_string):
    input_string += " "

    found_alphabets = {}
    loner_alphabets = set()

    for i in range(len(input_string) - 1):
        if input_string[i] != input_string[i + 1]:
            if input_string[i] in found_alphabets:
                loner_alphabets.add(input_string[i])
            else:
                found_alphabets[input_string[i]] = 1

    if len(loner_alphabets) == 0:
        return "N"

    answer = ''.join(sorted(loner_alphabets))
    return answer
