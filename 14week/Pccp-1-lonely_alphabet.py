import collections

def solution(input_string):
    answer = ''

    if len(input_string) == 1:
        return input_string
    
    stack = []
    stack.append(input_string[0])

    for i in range(1, len(input_string)):
        if input_string[i] != stack[-1]:
            stack.append(input_string[i])

    counter = collections.Counter(stack)

    for key, value in counter.items():
        if value >= 2:
            answer += key

    if len(answer) == 0:
        return "N"
    
    answer = ''.join(sorted(answer))
    return answer

# test case
# input_string	result
# "edeaaabbccd"	"de"
# "eeddee"	"e"
# "string"	"N"
# "zbzbz"	"bz"

#test code
if __name__ == '__main__':
    input_string = "eeddee"
    answer = solution(input_string)
    print(answer)