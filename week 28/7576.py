import copy
import sys
from collections import deque

# Initialize an empty deque
queue = deque()

M,N = map(int, input().split())

farm = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    farm.append(temp)

directions=[(-1,0),(0,-1),(1,0),(0,1)]

zcount=0
for m in range(M):
    for n in range(N):
        if farm[n][m]==1:
                queue.append((n,m,0))
                #print("initial 1 in",h," ",n, " ", m)
#print(farm)    
cur=0
while(queue):
    #print("loop entered")
    temp = queue.popleft()
    cur=temp[2]
    n=temp[0]
    m=temp[1]
    for d in directions:
        if (n+d[0]>=0 and n+d[0]<N) and (m+d[1]>=0 and m+d[1]<M):
            if farm[n+d[0]][m+d[1]]==0:
                #print("spread")
                farm[n+d[0]][m+d[1]]=1
                queue.append((n+d[0],m+d[1],cur+1))

zcount=0    
for m in range(M):
    for n in range(N):

            if farm[n][m]==0:
                zcount+=1
                break
       
    if zcount:
        break
    
if zcount:
    print(-1)
else:
    print(cur)
    
