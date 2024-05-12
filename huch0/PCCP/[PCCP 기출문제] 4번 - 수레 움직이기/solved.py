from collections import deque

EMPTY = 0
RED_START = 1
BLUE_START = 2
RED_END = 3
BLUE_END = 4
WALL = 5

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution(maze):
    def find_possible_moves(red_pos, blue_pos):
        def find_alone(pos, red_or_blue):
            moves = []

            for dx, dy in directions:
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != WALL:
                    if red_or_blue == 0 and (nx, ny) not in red_visited:
                        moves.append((nx, ny))
                    elif red_or_blue == 1 and (nx, ny) not in blue_visited:
                        moves.append((nx, ny))
            return moves

        pos_moves = []
        if red_pos == red_end:
            red_moves = [red_pos]
        else:
            red_moves = find_alone(red_pos, 0)

        if blue_pos == blue_end:
            blue_moves = [blue_pos]
        else:
            blue_moves = find_alone(blue_pos, 1)

        for red_new_pos in red_moves:
            for blue_new_pos in blue_moves:
                if red_new_pos == blue_pos and blue_new_pos == red_pos:
                    continue
                elif red_new_pos == blue_new_pos:
                    continue
                else:
                    pos_moves.append((red_new_pos, blue_new_pos))

        return pos_moves

    n = len(maze)
    m = len(maze[0])

    red_start, blue_start, red_end, blue_end = None, None, None, None

    for i in range(n):
        for j in range(m):
            if maze[i][j] == RED_START:
                red_start = (i, j)
            elif maze[i][j] == BLUE_START:
                blue_start = (i, j)
            elif maze[i][j] == RED_END:
                red_end = (i, j)
            elif maze[i][j] == BLUE_END:
                blue_end = (i, j)

    min_steps = n * m + 1
    red_visited, blue_visited = [], []
    stack = deque([(0, red_start, blue_start, red_visited, blue_visited)])

    while stack:
        step, red_pos, blue_pos, red_visited, blue_visited = stack.pop()

        # Mark as visited
        red_visited.append(red_pos)
        blue_visited.append(blue_pos)

        # Both finds the destinations
        if red_pos == red_end and blue_pos == blue_end:
            min_steps = min(min_steps, step)
            continue

        # Find possible next moves
        pos_moves = find_possible_moves(red_pos, blue_pos)

        for move in pos_moves:
            red_new_pos, blue_new_pos = move
            stack.append((step + 1, red_new_pos, blue_new_pos,
                         red_visited[:], blue_visited[:]))

    if min_steps == n * m + 1:
        return 0

    return min_steps
