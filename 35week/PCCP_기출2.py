def solution1(command):
    answer = []

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dir = 0
    nx, ny = 0, 0
    for c in command:
        cur_x, cur_y = nx, ny
        if c == "R":
            dir = (dir+1)%4
        elif c == "L":
            dir = dir-1
            if dir < 0:
                dir = 3
        elif c == "G":
            nx, ny = cur_x + dx[dir], cur_y + dy[dir]
        elif c == "B":
            nx, ny = cur_x - dx[dir], cur_y - dy[dir]

    answer = [nx, ny]
    return answer

import heapq

def solution2(ability, number):
    answer = 0
    heap = []
    for a in ability:
        heapq.heappush(heap, a)

    
    for i in range(number):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b)
        heapq.heappush(heap, a+b)

    answer = sum(heap)
    return answer

def solution3(menu, order, k):
    answer = 0
    
    stack = [0]
    for i in range(len(order)):
        s = stack[-1]
        if s < k*i:
            s = k*i
        s += menu[order[i]]
        stack.append(s)
    
    print(stack)
    max_count = 0
    check = [0 for _ in range(stack[-1]//k + 1)]
    for i in range(1, len(order)+1):
        count = min(stack[i]//k, len(order)) - (i-1)
        if check[stack[i]//k] == 0:
            if len(order) > stack[i]//k and stack[i] % k != 0:
                count += 1
            check[stack[i]//k] = 1
        if count > max_count:
            print(i)
            max_count = count
        print(i, end = " ")
        print(count)

    answer = max_count
    return answer