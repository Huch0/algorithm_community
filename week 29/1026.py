from collections import deque

N=int(input())

pic = [['a'] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    temp= list(input())
    pic[i]=temp[:]
    
directions=[(-1,0),(1,0),(0,-1),(0,1)]

def BFS(pic, visited, color, init):
    q=deque()
    q.append((init[0],init[1]))
    while q:
        temp_pair=q.popleft()
        x=temp_pair[0]
        y=temp_pair[1]
        for d in directions:
            if (x+d[0]>=0) and (x+d[0]<N) and (y+d[1]>=0) and (y+d[1]<N):
                newx=x+d[0]
                newy=y+d[1]
                if pic[newx][newy]==color and visited[newx][newy]==0:
                    visited[newx][newy]=1
                    q.append((newx,newy))
                    
Cpic=pic[:]            
Hcount=0
RGcount=0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            BFS(pic, visited, pic[i][j], (i,j))
            Hcount+=1
            if pic[i][j]=='G'or pic[i][j]=='R':
                RGcount+=1
        if pic[i][j]=='G':
            Cpic[i][j]='R'


visited = [[0] * N for _ in range(N)]
Ccount=0
for i in range(N):
    for j in range(N):
        if visited[i][j]== 0 and pic[i][j]=='R':
            BFS(Cpic, visited, 'R', (i,j))
            Ccount+=1

Ccount=Hcount-(RGcount-Ccount)

print(Hcount, ' ', Ccount)