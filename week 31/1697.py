from queue import Queue

# Create a queue
q = Queue()

FJ, cow = map(int, input().split())

field=[987654321]*100001

def BFS(start,end):
    q.put(start)
    field[start]=0
    while q:
        cur=q.get()
        if cur==end:
            break
        if cur+1<100001:
            if field[cur+1]>field[cur]+1:
                field[cur+1]=field[cur]+1
                q.put(cur+1)          
        if cur-1>=0:
            if field[cur-1]>field[cur]+1:
                field[cur-1]=field[cur]+1
                q.put(cur-1)
        if cur*2<100001:
            if field[cur*2]>field[cur]+1:
                field[cur*2]=field[cur]+1
                q.put(cur*2)
    print(field[end])

BFS(FJ, cow)