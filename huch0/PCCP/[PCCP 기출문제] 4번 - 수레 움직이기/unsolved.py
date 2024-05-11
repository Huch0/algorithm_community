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
                print((nx, ny), red_or_blue)
                # Out of range
                if nx < 0 or n <= nx or ny < 0 or m <= ny:
                    print(1)
                    continue
                # Wall
                elif maze[nx][ny] == WALL:
                    print(2)
                    continue
                # Already visited
                elif red_or_blue == 0 and (nx, ny) in red_visited:  # red
                    print(3, red_visited)
                    continue
                elif red_or_blue == 1 and (nx, ny) in blue_visited:  # blue
                    # print(3)
                    continue
                else:
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

        # print(red_moves, blue_moves)
        print(red_pos, blue_pos, red_moves, blue_moves)

        for red_new_pos in red_moves:
            for blue_new_pos in blue_moves:
                # Exchange their positions
                if red_new_pos == blue_pos and blue_new_pos == red_pos:
                    continue
                # Same cell simultaneously
                elif red_new_pos == blue_new_pos:
                    continue
                else:
                    pos_moves.append((red_new_pos, blue_new_pos))

        return pos_moves

    red_start = (0, 0)
    blue_start = (0, 0)
    red_end = (0, 0)
    blue_end = (0, 0)
    found = 0

    n = len(maze)
    m = len(maze[0])

    # Find start positions
    for i in range(n):
        for j in range(m):
            if maze[i][j] == RED_START:
                red_start = (i, j)
                found += 1
            elif maze[i][j] == BLUE_START:
                blue_start = (i, j)
                found += 1

            elif maze[i][j] == RED_END:
                red_end = (i, j)
                found += 1

            elif maze[i][j] == BLUE_END:
                blue_end = (i, j)
                found += 1

            if found == 4:
                break
        else:
            continue
        break

    print(red_start, blue_start, red_end, blue_end)

    # Start searching with dfs
    # Q = deque()
    # Q.append((0, red_start, blue_start))
    stack = deque()
    stack.append((0, red_start, blue_start))
    min_steps = n * m
    red_visited, blue_visited = [], []

    while stack:
        # step, red_pos, blue_pos = Q.popleft()
        step, red_pos, blue_pos = stack.pop()
        print(step, red_pos, blue_pos)

        # Mark as visited
        red_visited.append(red_pos)
        blue_visited.append(blue_pos)

        # Both finds their destinations
        if red_pos == red_end and blue_pos == blue_end:
            min_steps = min(min_steps, step)

        # Find new possible moves
        pos_moves = find_possible_moves(red_pos, blue_pos)
        # print(pos_moves)

        # Add next moves
        for move in pos_moves:
            red_pos, blue_pos = move
            # Q.append((step + 1, red_pos, blue_pos))
            stack.append((step + 1, red_pos, blue_pos))

    return min_steps
