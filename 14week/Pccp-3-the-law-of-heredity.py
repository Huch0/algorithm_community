match = {0: 'RR', 1: 'Rr', 2: 'Rr', 3: 'rr'}

def check(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return k%4
    elif n >= 3:
        type = check(n-1, k//4)
        if type == 0:
            return 0
        elif type == 3:
            return 3
        else:
            return k%4

def solution(queries):
    answer = []

    for query in queries:
        n, k = query
        answer.append(match[check(n, k-1)])

    return answer

# test case
# [[3, 5]]	["RR"]
# [[3, 8], [2, 2]]	["rr", "Rr"]
# [[3, 1], [2, 3], [3, 9]]	["RR", "Rr", "RR"]
# [[4, 26]]	["Rr"]

# test code
if __name__ == '__main__':
    queries = [[3, 5]]
    ret = solution(queries)
    print(ret)

    queries = [[3, 8], [2, 2]]
    ret = solution(queries)
    print(ret)

    queries = [[3, 1], [2, 3], [3, 9]]
    ret = solution(queries)
    print(ret)

    queries = [[4, 26]]
    ret = solution(queries)
    print(ret)