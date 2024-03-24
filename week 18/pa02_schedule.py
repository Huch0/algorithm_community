import heapq
import sys

# Set the recursion limit to 10000
sys.setrecursionlimit(10000)

def max_sum_range(arr):
    max_sum = float('-inf')
    max_start = None
    max_end = None

    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                max_start = i
                max_end = j

    return max_sum


workPerH, workEndT = map(int, input().split())
numTeams = int(input())

array = [workPerH] * (workEndT)

for i in range(numTeams):
    numTasks = int(input())
    for j in range(numTasks):
        start, end, noise = map(int, input().split())
        for k in range(start, end):
            array[k]+=noise

     
print(max_sum_range(array))