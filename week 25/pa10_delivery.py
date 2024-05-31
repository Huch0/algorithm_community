from itertools import permutations

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def total_path_distance(path):
    total_dist = 0
    cur_x, cur_y = 500, 500
    for step in path:
        if step > 0:  # Pickup
            total_dist += manhattan_distance(cur_x, cur_y, pickup[step - 1][0], pickup[step - 1][1])
            cur_x, cur_y = pickup[step - 1][0], pickup[step - 1][1]
        else:  # Delivery
            total_dist += manhattan_distance(cur_x, cur_y, destination[abs(step) - 1][0], destination[abs(step) - 1][1])
            cur_x, cur_y = destination[abs(step) - 1][0], destination[abs(step) - 1][1]
    return total_dist

def branch_and_bound(n, pickup, destination):
    best_distance = float('inf')
    best_paths = []
    
    def search(path, cur_x, cur_y, carried, total_dist):
        nonlocal best_distance, best_paths
        
        if len(path) == 2 * n:
            if total_dist < best_distance:
                best_distance = total_dist
                best_paths = [path[:]]
            elif total_dist == best_distance:
                best_paths.append(path[:])
            return
        
        if len(carried) < 2:
            for i in range(n):
                if i + 1 not in path:
                    next_x, next_y = pickup[i]
                    new_dist = total_dist + manhattan_distance(cur_x, cur_y, next_x, next_y)
                    if new_dist <= best_distance:  # allow paths with the same distance
                        search(path + [i + 1], next_x, next_y, carried + [i + 1], new_dist)
        
        for i in carried:
            next_x, next_y = destination[i - 1]
            new_dist = total_dist + manhattan_distance(cur_x, cur_y, next_x, next_y)
            if new_dist <= best_distance:  # allow paths with the same distance
                new_carried = carried[:]
                new_carried.remove(i)
                search(path + [-i], next_x, next_y, new_carried, new_dist)
    
    search([], 500, 500, [], 0)
    
    # Find the lexicographically smallest path among the best paths
    best_path = min(best_paths) if best_paths else []
    
    return best_path, best_distance

# Input
n = int(input())
pickup = []
destination = []

for _ in range(n):
    temp = list(map(int, input().split()))
    pickup.append((temp[0], temp[1]))
    destination.append((temp[2], temp[3]))

# Solve using Branch and Bound
solution, total_distance = branch_and_bound(n, pickup, destination)

# Print solution and total distance
print(' '.join(map(str, solution)))
print(total_distance)
