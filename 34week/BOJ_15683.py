from copy import deepcopy

N, M = map(int, input().split())

room = []
cctvs = []

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(N):
    line = input().split()
    for j in range(len(line)):
        if line[j] != '0' and line[j] != '6':
            cctvs.append([line[j],i,j,0])
    room.append(line)

def watch(cctv):
    global room
    #print(cctv)
    cur_x, cur_y = cctv[1], cctv[2]
    cctv_type = cctv[0]
    c_dir = cctv[3]
    cctv_dir = []
    if cctv_type == '5':
        cctv_dir = [0, 1, 2, 3]

    elif cctv_type == '2':
        dir_table = [[0,1], [2,3]]
        cctv_dir = dir_table[c_dir]

    elif cctv_type == '1':
        cctv_dir = [c_dir]

    elif cctv_type == '3':
        dir_table = [[0,2], [0,3], [1,2], [1,3]]
        cctv_dir = dir_table[c_dir]

    elif cctv_type == '4':
        dir_table = [[0,1,2], [0,1,3], [0,2,3], [1,2,3]]
        cctv_dir = dir_table[c_dir]

    for dir in cctv_dir:
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        while 0 <= nx < N and 0 <= ny < M:
            if room[nx][ny] == '6':
                break
            if room[nx][ny] == '0':
                room[nx][ny] = '#'
            nx = nx + dx[dir]
            ny = ny + dy[dir]

    count = count_blind()

    # for l in room:
    #     for i in range(len(l)):
    #         print(l[i], end = " ")
    #         if l[i] == '#':
    #             l[i] = '0'
    #     print()
    
    return count 

def count_blind():
    count = 0
    for i in range(N):
        count += room[i].count('0')
    return count

is_used = [False] * len(cctvs)

min_count = N*M

# def print_room():
#     global room
#     for l in room:
#         for i in range(len(l)):
#             print(l[i], end= " ")
#         print()

def fun(n):
    if n == len(cctvs):
        global min_count, room
        original_room = deepcopy(room)
        for cctv in cctvs:
            watch(cctv)
        #print_room()
        count = count_blind()
        room = deepcopy(original_room)
        if count < min_count:
            min_count = count
        return
    
    # for i in range(len(cctvs)):
    #     if not is_used[i]:
    #         is_used[i] = True
    #case 2:
    if cctvs[n][0] == '2':
        for j in range(2):
            cctvs[n][3] = j
            fun(n+1)
    #case 5:
    elif cctvs[n][0] == '5':
        cctvs[n][3] = 0
        fun(n+1)
    else:
        for j in range(4):
            cctvs[n][3] = j
            fun(n+1)
    #is_used[i] = False

fun(0)
print(min_count)