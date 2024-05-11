import sys
import heapq
INF=987654321

DIRECTIONS={(1,0),(0,1),(-1,0),(0,-1)}

m, n = map(int,  sys.stdin.readline().split())
# Create a matrix with all ones
adjMatrix = [[1 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
hMatrix= [[INF for _ in range(n)] for _ in range(m)]

grayCellsNum=int(input())

for i in range(grayCellsNum):
    _, x, y = map(int,  sys.stdin.readline().split())
    adjMatrix[x][y]=0

user_input = input()
_, x, y = user_input.split()
x, y = int(x), int(y)
visited[x][y]=1
start = (x,y)

user_input = input()
_, x, y = user_input.split()
x, y = int(x), int(y)
goal= (x,y)

user_input = input()
_, obNum=user_input.split()
obNum=int(obNum)

for i in range(obNum):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for j in range(x1,x2+1):
        for k in range(y1, y2+1):
            adjMatrix[j][k]=0
   
#for e in adjMatrix:
    #print(e)
    
def hFunc(x,y):
    global goal
    #return int(math.sqrt(abs(x-goal[0])*abs(x-goal[0])+abs(y-goal[1])*abs(y-goal[1])))
    a=abs(x-goal[0])
    b=abs(y-goal[1])
    #temp=a*a+b*b
    temp=a+b
    hMatrix[x][y]=temp
    return temp

#def gFunc(x,y):
#    global start
#    return abs(start[0]-x)+abs(start[1]-y)

cur_x=start[0]
cur_y=start[1]

count=1
while(cur_x!=goal[0] or cur_y!=goal[1]):
    best=INF
    best_dir=(0,0)
    
    for p in DIRECTIONS:
        if(cur_x+p[0]>0 and cur_x+p[0]<m and cur_y+p[1]>0 and cur_y+p[1]<m and adjMatrix[cur_x+p[0]][cur_y+p[1]]==1 and visited[cur_x+p[0]][cur_y+p[1]]==0):
            if(hMatrix[cur_x+p[0]][cur_y+p[1]]!=INF):
                temp=hMatrix[cur_x+p[0]][cur_y+p[1]]
            else:
                temp=hFunc(cur_x+p[0], cur_y+p[1])
            #gFunc(cur_x+p[0], cur_y+p[1])
            if(best>temp):
                best=temp
                best_dir=(p[0],p[1])
    cur_x+=best_dir[0]
    cur_y+=best_dir[1]
    visited[cur_x][cur_y]=1
    #print("going to")
    #print(cur_x)
    #print(',')
    #print(cur_y)
    count+=1
    #for e in visited:
        #print(e)
    
#for e in hMatrix:
    #print(e)
print((count-1)*3)

   
        
