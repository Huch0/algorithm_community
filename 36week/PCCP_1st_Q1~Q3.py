from collections import deque

def solution1(input_string):
    answer = ''
    
    stack = deque()
    stack.append(input_string[0])
    
    for i in input_string[1:]:
        if i != stack[-1]:
            if i in stack and i not in answer:
                answer += i
            stack.append(i)
    if answer == "":
        return "N"
    else:
        return "".join(sorted(answer))
    
from itertools import permutations

def solution2(ability):
    answer = 0
    perm = permutations(range(len(ability)), len(ability[0]))
    
    for p in perm:
        a = 0
        i = 0
        for n in p:
            a += ability[n][i]
            i += 1
        if a > answer:
            answer = a
    
    return answer

# # Using DP
# def solution3(queries):
    
    # answer = []
    # D = [[] for _ in range(17)]
    # D[1] = ["Rr"]
    
    
    # for i in range(2, 17):
    #     c = []
    #     for j in range(4**(i-2)):
    #         if D[i-1][j] == "RR":
    #             c += ["RR" for _ in range(4)]
    #         elif D[i-1][j] == "Rr":
    #             c += ["RR", "Rr", "Rr", "rr"]
    #         else:
    #             c += ["rr" for _ in range(4)]
                
    #     D[i] = c
    # print(D)
    # for q in queries:
    #     answer.append(D[q[0]][q[1]-1])
    
    # return answer

def fun(g, i):
    if g == 1 and i == 0:
        return "Rr"
    elif g == 2:
        p = ["RR", "Rr", "Rr", "rr"]
        return p[i]
    
    p = fun(g-1, i//4)
    if p == "RR":
        return "RR"
    elif p == "Rr":
        pool = ["RR", "Rr", "Rr", "rr"]
        return pool[i%4]
    else:
        return "rr"

def solution3(queries):
    answer = []
    
    for q in queries:
        answer.append(fun(q[0], q[1]-1))
    return answer
