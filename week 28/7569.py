import copy
import sys
from collections import deque

# Initialize an empty deque
queue = deque()

M,N,H = map(int, input().split())

farm = []

for j in range(H):
    story = []
    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        story.append(temp)
    farm.append(story)

directions=[(-1,0,0),(0,-1,0),(0, 0, -1),(1,0,0),(0,1,0),(0, 0, 1)]

zcount=0
for m in range(M):
    for n in range(N):
        for h in range(H):
            if farm[h][n][m]==1:
                queue.append((h,n,m,0))
                #print("initial 1 in",h," ",n, " ", m)
#print(farm)    
cur=0
while(queue):
    #print("loop entered")
    temp = queue.popleft()
    cur=temp[3]
    h=temp[0]
    n=temp[1]
    m=temp[2]
    for d in directions:
        if (h+d[0]>=0 and h+d[0]<H) and (n+d[1]>=0 and n+d[1]<N) and (m+d[2]>=0 and m+d[2]<M):
            if farm[h+d[0]][n+d[1]][m+d[2]]==0:
                #print("spread")
                farm[h+d[0]][n+d[1]][m+d[2]]=1
                queue.append((h+d[0],n+d[1],m+d[2],cur+1))

zcount=0    
for m in range(M):
    for n in range(N):
        for h in range(H):
            if farm[h][n][m]==0:
                zcount+=1
                break
        if zcount:
            break
    if zcount:
        break
    
if zcount:
    print(-1)
else:
    print(cur)
    
