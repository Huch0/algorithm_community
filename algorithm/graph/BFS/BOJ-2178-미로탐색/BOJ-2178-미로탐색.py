import sys
from collections import deque, defaultdict


row, column = list(map(int,sys.stdin.readline().split()))

matrix = []
for i in range(row) :
    matrix.append(list(map(int,list(sys.stdin.readline())[:-1])))

"""
queue = deque([((0,0),1)])  
cost = defaultdict(int)

while queue :
    def check(x,y) :
        if x > row-1 or x < 0 or y > column-1 or y < 0 : return False
        else : return True
        
    pop = queue.pop()
    x,y = pop[0][0],pop[0][1]
    weight = pop[1]
    
    if (x,y) not in cost or cost[(x,y)] > weight:
        cost[(x,y)] = weight
        if check(x+1, y) and matrix[x+1][y]: queue.append(((x+1, y),weight+1))
        if check(x-1, y) and matrix[x-1][y]: queue.append(((x-1, y),weight+1))
        if check(x, y+1) and matrix[x][y+1]: queue.append(((x, y+1),weight+1))
        if check(x, y-1) and matrix[x][y-1]: queue.append(((x, y-1),weight+1))
        
print(cost[(row-1,column-1)])
"""

import heapq

heap = [(1,(0,0))]
cost = defaultdict(int)

while True :
    def check(x,y) :
        if x > row-1 or x < 0 or y > column-1 or y < 0 : return False
        else : return True
        
    pop = heapq.heappop(heap)
    x,y = pop[1][0], pop[1][1]
    weight = pop[0]
    if (x,y) == (row-1,column-1) :
        cost[(x,y)] = weight
        break
    
    if (x,y) not in cost :
        cost[(x,y)] = weight
        if check(x+1, y) and matrix[x+1][y]: heapq.heappush(heap,(weight+1,(x+1,y)))
        if check(x-1, y) and matrix[x-1][y]: heapq.heappush(heap,(weight+1,(x-1,y)))
        if check(x, y+1) and matrix[x][y+1]: heapq.heappush(heap,(weight+1,(x,y+1)))
        if check(x, y-1) and matrix[x][y-1]: heapq.heappush(heap,(weight+1,(x,y-1)))

print(cost[(row-1,column-1)])

