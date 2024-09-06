import heapq
import sys

N=int(sys.stdin.readline())
paper = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    paper[i]=list(map(int, sys.stdin.readline().split()))
 
blue_count=0
white_count=0
    
def folding(to_fold):
    global blue_count, white_count
    #print("entered")
    blue=0
    white=0
    sum=0
    
    size=len(to_fold)
        
    #print("paper size:",size)
    for row in to_fold:
        for e in row:
            sum+=e
    
    if sum==size*size:
        blue+=1
    elif sum==0:
        white+=1
    else:
        folding([row[:size//2] for row in to_fold[:size//2]])
        folding([row[size//2:] for row in to_fold[:size//2]])
        folding([row[:size//2] for row in to_fold[size//2:]])
        folding([row[size//2:] for row in to_fold[size//2:]])
                
    blue_count+=blue
    white_count+=white    
       
folding(paper)

print(white_count)
print(blue_count)