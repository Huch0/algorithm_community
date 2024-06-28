# 3
# 2 2 2
# 4 4 4
# 8 8 8
from collections import deque
import copy

N = int(input())

board = []

max_num = 0

for _ in range(N):
    line = input().split()
    board.append([int(l) for l in line])
    max_num = max(max(board[-1]), max_num)


# def transpose(matrix):
#         new_board = copy.deepcopy(matrix)
#         for i in range(N):
#             for j in range(N):
#                 new_board[i][j] = board[j][i]
#         return new_board

# print(transpose(board))

# def merge_right(line):
#     stack = deque()
#     for i in range(len(line)):
#         if line[i] != 0:
#             if stack:
#                 if stack[-1][0] == line[i] and stack[-1][1] == 0:
#                     stack.pop()
#                     stack.append((2*line[i], 1))
#                 else:
#                     stack.append((line[i], 0))
#             else:
#                 stack.append((line[i], 0))
#     new_line = [0 for _ in range(len(line))]
#     i = len(line)-1
#     while stack:
#         new_line[i] = stack.pop()[0]
#         i -= 1
#     return new_line

# print(merge_right([0, 2, 4, 4, 8, 16]))


def cal_max(board):
    result = 0
    for i in range(N):
        result = max(max(board[i]), result)
    return result

# dir : 0~3 -> 상/하/좌/우
def action(dir, board):
    new_board = copy.deepcopy(board)
    def merge(line):
        stack = deque()
        for i in range(N):
            if line[i] != 0:
                if stack:
                    if stack[-1][0] == line[i] and stack[-1][1] == 0:
                        stack.pop()
                        stack.append((2*line[i], 1))
                    else:
                        stack.append((line[i], 0))
                else:
                    stack.append((line[i], 0))
        new_line = [0 for _ in range(N)]
        i = 0
        while stack:
            new_line[i] = stack.popleft()[0]
            i += 1
        return new_line

    def merge_right(line):
        stack = deque()
        for i in range(N):
            if line[i] != 0:
                if stack:
                    if stack[-1][0] == line[i] and stack[-1][1] == 0:
                        stack.pop()
                        stack.append((2*line[i], 1))
                    else:
                        stack.append((line[i], 0))
                else:
                    stack.append((line[i], 0))
        new_line = [0 for _ in range(N)]
        i = N-1
        while stack:
            new_line[i] = stack.pop()[0]
            i -= 1
        return new_line

    def transpose(matrix):
        new_matrix = copy.deepcopy(matrix)
        for i in range(N):
            for j in range(N):
                new_matrix[i][j] = matrix[j][i]
        return new_matrix


    if dir < 2:
        board = transpose(board)
        #print(f"board : {board}")
        if dir == 0:
            for i in range(N):
                new_board[i] = merge(board[i])[:]
        else:
            for i in range(N):
                new_board[i] = merge_right(board[i])[:]
        new_board = transpose(new_board)
    else:
        if dir == 2:
           for i in range(N):
                new_board[i] = merge(board[i])[:]
        else:
            for i in range(N):
                new_board[i] = merge_right(board[i])[:]
    return new_board

# BFS

queue = deque()
# visited = [False for _ in range(1385)]
queue.append((0, 0, board))
# visited[0] = True
result = 0
while queue:
    cur_x, cur_y, board = queue.popleft()
    if cur_x == 5:
        result = max(result, cal_max(board))
        #print(board)
        continue
    for dir in range(4):
        nx, ny = cur_x + 1, 4 * cur_y + dir
        new_board = action(dir, board)
        #if cur_x == 0:
            #print(new_board)
        queue.append((nx, ny, new_board))

print(result)
