import heapq

def solution(program):
    answer = [0 for _ in range(11)]
    len_program = len(program)
    program.sort(key = lambda x : x[1])
#    print(program)
    heap = []
    time = program[0][1]
    i = 0
    while True:
        while i < len_program and program[i][1] <= time:
            heapq.heappush(heap, program[i])
            i += 1

#        print(heap)

        if not heap:
            if i >= len_program:
                break
            else:
                time = program[i][1]
                continue
            
        p = heapq.heappop(heap)
        answer[p[0]] += (time - p[1])
        time += p[2]
        
    answer[0] = time
    return answer

# program = [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]
# print(solution(program))