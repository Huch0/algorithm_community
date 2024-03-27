import sys
import collections

case = int(sys.stdin.readline())

for i in range(case) :
    length, target_index = list(map(int,sys.stdin.readline().split()))
    
    deque = collections.deque(list(map(int,sys.stdin.readline().split())))
    
    max_importance = max(deque)
    
    for j in range(length) :
        if j == target_index : deque.append((deque.popleft(),True))
        else : deque.append((deque.popleft(),False))
    
    index = 1
    while True :
        pop = deque.popleft()
        if pop[0] == max_importance : 
            if pop[1] : 
                print(index)
                break
            else : 
                max_importance = max(deque)[0]
                index += 1
                continue
        
        else : deque.append(pop)
            

    