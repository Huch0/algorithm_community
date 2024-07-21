import queue
import sys

t = int(sys.stdin.readline().strip())
    
def left (t):
    temp=t//1000
    t=(t*10+temp)%10000
    return t

def right (t):
    temp=t%10
    t=temp*1000+t//10
    return t

for _ in range(t):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    visited=[False]*10000
    q = queue.Queue()
    visited[a]=True
    if a==0:        
        q.put((9999,"S"))
        visited[9999]=True
    else:
        q.put(((a<<1)%10000,"D"))
        visited[(a<<1)%10000]=True
        q.put((a-1,"S"))
        visited[a-1]=True
    q.put((left(a),"L"))
    visited[left(a)]=True
    q.put((right(a),"R"))
    visited[right(a)]=True
    
    while q:
        temp_pair= q.get()
        a=temp_pair[0]
        if a == b:
            print(temp_pair[1])
            break
        
        if a==0 and visited[9999]==False:
            q.put((9999,temp_pair[1]+'S'))
            visited[9999]=True
        else:
            temp=(a<<1)%10000
            if visited[temp]==False:
                q.put((temp,temp_pair[1]+'D'))
                visited[temp]=True
            temp=a-1
            if visited[temp]==False:
                q.put((a-1,temp_pair[1]+'S'))
                visited[temp]=True
            
            
        if (temp_pair[1][-4:]=="LLL") or (temp_pair[1][-4:]=="RRR"):
            continue
        else:
            temp=left(a)
            if temp_pair[1][-1]!='R' and visited[temp]==False:
                q.put((temp,temp_pair[1]+'L'))
                visited[temp]=True
            temp=right(a)
            if temp_pair[1][-1]!='L' and visited[temp]==False:
                q.put((temp,temp_pair[1]+'R'))
                visited=[temp]=True
