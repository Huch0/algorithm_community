import heapq


def solution(program):
    answer = [0] * 11  # Initialize

    program.sort(key=lambda x: (x[1], x[0]))  # Sort by called time, priority

    ready_q = [program.pop(0)]  # Push the first program to the ready_q
    end_time = ready_q[0][1]  # For the case of start time is not 0.
    for i in range(len(program) + 1):  # +1 as we already pop the first program
        runner = heapq.heappop(ready_q)

        if runner[1] < end_time:  # The called time is before current end_time
            # Add delay time to the answer
            answer[runner[0]] += end_time - runner[1]
            # runner will start execution at current end_time
            end_time += runner[2]
        else:
            end_time = runner[1] + runner[2]

        while program:
            # Push to ready_q only called time is before current end_time
            if end_time < program[0][1]:
                # For the case of next runner has no delay
                if not ready_q:
                    heapq.heappush(ready_q, program.pop(0))
                break

            heapq.heappush(ready_q, program.pop(0))

    answer[0] = end_time
    return answer
