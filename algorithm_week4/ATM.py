def get_input():
    num = int(input())
    time_list = list(map(int, input().split()))
    return time_list

time_list = get_input()
time_list.sort()

sum = 0
part_sum = 0

for time in time_list:
    part_sum += time
    sum += part_sum
    
print(sum)