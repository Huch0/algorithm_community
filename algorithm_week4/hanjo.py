hill_num = int(input())
hill_list = list(map(int, input().split()))
kill = 0
kill_list = []
cur_hill = hill_list[0]

for i in range(1, len(hill_list)):
    if cur_hill > hill_list[i]:
        kill += 1
    else:
        cur_hill = hill_list[i]
        kill_list.append(kill)
        kill = 0
    if i == len(hill_list)-1:
        kill_list.append(kill)
        
max_kill = max(kill_list)
print(max_kill)