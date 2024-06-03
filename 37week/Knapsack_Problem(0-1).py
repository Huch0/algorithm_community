from collections import deque

jewelry = [[], [40, 2], [30, 5], [50, 10], [10, 5]]

W = 16
max_profit = 0
include = []

def promising(i, w, p):
    total_w, j, k = 0, 0, 0
    bound = 0
    if w >= W:
        #print(f"bound : None")
        return False
    else:
        j = i+1
        bound = p
        total_w = w
        while j < len(jewelry) and total_w + jewelry[j][1] <= W:
            bound = bound + jewelry[j][0]
            total_w += jewelry[j][1]
            j += 1
        k = j
        if k < len(jewelry):
            bound += (W-total_w) * jewelry[k][0] / jewelry[k][1]
    print(f"bound : {bound}")
    return bound > max_profit

count_1 = 0

def knapsack1(i, profit, weight):
    global max_profit, count_1
    count_1 += 1
    
    if weight <= W:
        print(f"i : {i}\tprofit : {profit}\tweight : {weight}", end= "\t")
    else:
        print(f"i : {i}\tprofit : {profit}\tweight : {weight}\tbound : None")
    
    if weight <= W and profit > max_profit:
        max_profit = profit
        # num_best = i
        # bestset = include

    if promising(i, weight, profit):
        include.append(i+1)
        knapsack1(i+1, profit + jewelry[i+1][0], weight + jewelry[i+1][1])
        include.pop()
        knapsack1(i+1, profit, weight)

print()
print()
print("Using BackTracking")
print("---------------------------------------------------------")
knapsack1(0, 0, 0)
print("---------------------------------------------------------")
print(f"max_profit : {max_profit}\t call counter : {count_1}")
print("---------------------------------------------------------")

max_profit_2 = 0
count_2 = 0

def promising2(i, w, p):
    total_w, j, k = 0, 0, 0
    bound = 0
    if w >= W:
        #print(f"bound : None")
        return False
    else:
        j = i+1
        bound = p
        total_w = w
        while j < len(jewelry) and total_w + jewelry[j][1] <= W:
            bound = bound + jewelry[j][0]
            total_w += jewelry[j][1]
            j += 1
        k = j
        if k < len(jewelry):
            bound += (W-total_w) * jewelry[k][0] / jewelry[k][1]
    print(f"bound : {bound}")
    return bound > max_profit_2

def knapsack2():
    global max_profit_2, count_2    
    queue = deque()
    root = (0,0,0)
    queue.append(root)

    while queue:
        i, p, w = queue.popleft()
        if w <= W:
            print(f"i : {i}\tprofit : {p}\tweight : {w}", end= "\t")
        else:
            print(f"i : {i}\tprofit : {p}\tweight : {w}\tbound : None")
        if w <= W and p > max_profit_2:
            max_profit_2 = p

        if promising2(i, w, p):
            queue.append((i+1, p+jewelry[i+1][0], w+jewelry[i+1][1]))
            count_2 += 1
            queue.append((i+1, p, w))
            count_2 += 1

print()
print()
print("Using BFS")
print("---------------------------------------------------------")
knapsack2()
print("---------------------------------------------------------")
print(f"max_profit : {max_profit_2}\t call counter : {count_2}")
print("---------------------------------------------------------")

import heapq


max_profit_3 = 0
count_3 = 0

def promising3(i, w, p):
    total_w, j, k = 0, 0, 0
    bound = 0
    if w >= W:
        return 0
    else:
        j = i+1
        bound = p
        total_w = w
        while j < len(jewelry) and total_w + jewelry[j][1] <= W:
            bound = bound + jewelry[j][0]
            total_w += jewelry[j][1]
            j += 1
        k = j
        if k < len(jewelry):
            bound += (W-total_w) * jewelry[k][0] / jewelry[k][1]
    #print(f"bound : {bound}")
    return bound

def knapsack3():
    global max_profit_3, count_3
    heap = []
    root = (-promising3(0, 0, 0), 0, 0, 0)
    heapq.heappush(heap, root)  
    count_3 += 1

    while heap:
        b, i, p, w = heapq.heappop(heap)
        b *= -1

        if w <= W:
            print(f"i : {i}\tprofit : {p}\tweight : {w}\tbound : {b}")
        else:
            print(f"i : {i}\tprofit : {p}\tweight : {w}\tbound : None")

        if b > max_profit_3:
            if (w <= W and p > max_profit_3):
                max_profit_3 = p
            
            new_b = promising3(i+1, w+jewelry[i+1][1], p+jewelry[i+1][0])
            if new_b > max_profit_3:
                heapq.heappush(heap, (-new_b, i+1, p+jewelry[i+1][0], w+jewelry[i+1][1]))
                count_3 += 1

            new_b_2 = promising3(i+1, w, p)
            heapq.heappush(heap, (-new_b_2, i+1, p, w))
            count_3 += 1

print()
print()
print("Using Best-First Search with Branch and Bound")
print("---------------------------------------------------------")
knapsack3()
print("---------------------------------------------------------")
print(f"max_profit : {max_profit_3}\t call counter : {count_3}")
print("---------------------------------------------------------")